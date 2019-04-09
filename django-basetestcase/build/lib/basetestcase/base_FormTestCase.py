from .base_UtilityTestCase import UtilityTestCase


class FormTestCase(UtilityTestCase):
    
    def form_field_test(self, field, error_messages={}, help_text='', initial=None, label='', required=True, widget_attrs={}):
        form = self.form()
        try:
            form.fields[field]
        except KeyError:
            raise Exception(f'\n   Form does not have field\n\n   {field}')
        
        completed_attrs = []
        for attr, expected in widget_attrs.items():
            try:
                actual = form.fields[field].widget.attrs[attr]
            except KeyError:
                raise Exception(
                    f'\n   {attr} for form field {field} has not been set.'
                )
          
            self.assertEquals(expected, actual, msg=f'\n   {field}: {attr}')
            completed_attrs.append(attr)
            
        for attr, actual in form.fields[field].widget.attrs.items():
            if attr not in completed_attrs:
                raise Exception(f'\n  {field}:{attr} is set and should not be.')
        
        if required is True and 'required' not in error_messages:
            error_messages['required'] = 'This field is required.'
        elif len(error_messages) is not 0:
            for error, error_message in error_messages.items():
                actual_error_message = form.fields[field].error_messages[error]
            
            self.assertEquals(
                error_message,
                actual_error_message,
                msg=f'\n   {field}: error_message[{error}]'
            )
            
        actual_help_text = form.fields[field].help_text
        self.assertEquals(
            help_text,
            actual_help_text,
            msg=f'\n   {field}: help_text'
        )
            
        actual_initial = form.fields[field].initial
        self.assertEquals(
            initial,
            actual_initial,
            msg=f'\n   {field}: initial value'
        )
        
        actual_label = form.fields[field].label
        self.assertEquals(
            label,
            actual_label,
            msg=f'\n{field}: label'
        )
        
        actual_required = form.fields[field].required
        self.assertEquals(
            required,
            actual_required,
            msg=f'\n   {field}: required'
        )
    
    
    def form_required_field_error_test(self, data={}, error_messages={}):
        required_fields = []
        Form = self.form()
        for field in Form.fields:
            if Form.fields[field].required is True:
                required_fields.append(field)

        for field, value in data.items():
            if field in required_fields:
                _data = {**data}
                _data[field] = ''
                form = self.form(data={**_data})
            
                self.assertFalse(
                    form.is_valid(),
                    msg=f'\n   Form should not be valid.\n   {field} should be blank.\n   data={_data}'
                )
                error = 'This field is required.'
                if field in error_messages:
                    error = error_messages[field]
                self.assertEqual(
                    form.errors[field],
                    [error],
                    msg=f'{field}'
                )
    
    
    def formset_error_test(self, formset, form_index=None, field=None, message=''):
        if form_index is None and field is None:
            self.assertEqual(formset.non_form_errors(), [message])
        if field is None:
            self.assertEqual(formset[form_index].non_field_errors(), [message])
        else:
            self.assertEqual(formset[form_index].errors[field], [message])
    
    
    def formset_test(self, can_delete=False, extra=1, field_data={}, form=None, formset=None, initial=0, max_num=None, min_num=None, model=None, prefix='form', total=1, validate_max=False, validate_min=False):
        form_data, test_model_instances = self.formset_filler(
            field_data=field_data,
            initial=initial,
            model=model,
            prefix=prefix,
            total=total
        )
        test_formset = formset(form_data, prefix=prefix)
        self.assertEqual(test_formset.extra, extra)
        
        if form is not None:
            self.assertTrue(issubclass(test_formset.form, form))
        
        if max_num is not None:
            self.assertEqual(test_formset.max_num, max_num)
        
        if min_num is not None:
            self.assertEqual(test_formset.min_num, min_num)
        self.assertEqual(test_formset.can_delete, can_delete)
        self.assertEqual(test_formset.prefix, prefix)
        self.assertEqual(test_formset.validate_max, validate_max)
        self.assertEqual(test_formset.validate_min, validate_min)
        if test_formset.is_valid():
            test_formset.save()
            if model is not None:
                self.instances_saved_test(model, test_model_instances, total)
        else:
            self.fail(
                f'formset is not valid.\n{data}\n{test_formset.non_form_errors()}\n{test_formset.errors}'
            )