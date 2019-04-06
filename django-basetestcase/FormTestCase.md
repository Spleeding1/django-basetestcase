
# FormTestCase

```python
from basetestcase import FormTestCase
```

- [Test class setup](#Test-class-setup)
- [form_field_test()](#form_field_test)
- [form_required_field_error_test()](#form_required_field_error_test)
- [formset_error_test()](#formset_error_test)
- [formset_test()](#formset_test)

```python
from django.forms import ModelForm,modelformset_factory, TextInput

from .models import MyModel

class MyForm(ModelForm):
    
    class Meta:
        model = MyModel
        fields = '__all__'
        
        widgets = {
            'field_1': TextInput(
                attrs={
                    'autofocus': 'autofocus',
                    'class': 'form-control',
                    'placeholder': 'Field 1',
        })}


MyFormSet = modelformset_factory(
    MyModel,
    can_delete=True,
    extra=3,
    form=MyForm,
    max_num=7,
    validate_max=True
)
```

# Test class setup

There is a required method as a part of using this test class.

```python
def form(self, *args, **kwargs):
        form = MyForm(*args, **kwargs)
        return form
```

## form_field_test()
Tests the setup of a `Form`'s field.

```python
def form_field_test(self, field, error_messages={}, help_text='',
    initial=None, label='', required=True, widget_attrs={})
```

- field: A string of the Model's field name.
- error_messages: A dictionary of the `error_messages`.
- help_text: Tests the `help_text` set on the field.
- initial: Tests the `initial` value.
- label: Tests field's `label`.
- required: Tests if the field is `required`.
- widget_attrs: A dictionary of all of the field attrs.<br />
    - Will raise an error for an attr set on the field not listed here.<br />
    - Should handle almost anything you throw at it.

```python
def test_field_rendered(self):
    self.form_field_test(
        'field_1',
        help_text='This is help text.',
        label='Field 1',
        widget_attrs={
            'autofocus': 'autofocus',
            'class': 'form-control',
            'maxlength': '50',
            'placeholder':'Field 1',
    })
```

## form_required_field_error_test()
Takes a dictionary of the required values of the `Form` and
loops through them setting each one to a empty string, testing
each loop for `form.is_valid() == False`.

```python
def form_required_field_error_test(self, data={}, error_messages={})
```
- data: A dictionary with a valid value for each `required` field.
- error_messages: A dictionary with `field: required_error_message` pair.<br />
    - Default `error_message` is `'This field is required.`

```python
self.form_required_field_error_test(
    data = {
        'field_1': 'This is field one.',
        'field_2': 'This is field two.',
})
```

## formset_error_test()
Similar to the [`assertFormsetError`](#https://docs.djangoproject.com/en/2.1/topics/testing/tools/#django.test.SimpleTestCase.assertFormsetError), except does not require `response`.

```python
def formset_error_test(self, formset, form_index=None, field=None, message='')
```

## formset_test()
Tests a `formset`, including populating data and testing if instances<br />
were saved in a given `Model`. It uses both [`formset_filler`](https://github.com/Spleeding1/django-basetestcase/blob/master/django-basetestcase/UtilityTestCase.md) and a<br />
[`instances_saved_test`](https://github.com/Spleeding1/django-basetestcase/blob/master/django-basetestcase/UtilityTestCase.md) methods.

```python
def formset_test(self, formset=None, can_delete=False, extra=1, field_data={},
    form=None, initial=0, max_num=None, min_num=None, model=None, prefix='form',
    total=1, validate_max=False, validate_min=False)
```

- formset: The `formset` being tested.
- can_delete: Tests if `can_delete` is set to `True` or `False`.
- extra: Tests the number of `extra` forms.
- field_data: One `form`s worth of valid data. It uses this data and<br />
generates to fill the formset.
- form: Tests what `form` is used.
- initial: The number of `INITIAL_FORMS`. Generates these as well.
- max_num: Tests the value set in `max_num`.
- min_num: Tests the value set in `min_num`.
- model: If given, tests that all of the `instances` generated were saved.
- prefix: The name of the `prefix` intended to be used.
- total: The `TOTAL_FORMS` in the `formset`.
- validate_max: Tests if `validate_max` is `True` or `False`.
- validate_min: Tests if `validate_min` is `True` or `False`.

```python
self.formset_test(
    can_delete=True,
    extra=2,
    field_data={
        'field_1': 'I am field one.',
        'field_2': 'I am field two.',
    },
    form=MyForm,
    formset=MyFormSet,
    initial=8,
    model=MyModel,
    prefix='my_prefix',
    total=10,
)
```
