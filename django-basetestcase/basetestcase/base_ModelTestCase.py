from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse


class ModelTestCase(TestCase):
    
    def model_field_test(self, field, blank=False, choices=None, default=None, error_messages=None, help_text=None, max_length=None, null=False, unique=False, verbose_name=''):
        Model = self.model()
        
        blank_value = Model._meta.get_field(field).blank
        self.assertEquals(blank, blank_value, msg=f'\n   {field}: blank')
        
        if choices is not None:
            actual_choices = Model._meta.get_field(field).choices
            self.assertEquals(
                choices,
                actual_choices,
                msg=f'\n   {field}: choices'
            )
        
        if default is not None:
            actual_default = Model._meta.get_field(field).default
            self.assertEquals(
                default,
                actual_default,
                msg=f'\n   {field}: default'
            )
        
        if error_messages is not None:
            for code, error in error_messages.items():
                actual_error = Model._meta.get_field(field).error_messages[code]
                self.assertEquals(
                    error,
                    actual_error,
                    msg=f'\n   {field}: error_message'
                )
        
        if help_text is not None:
            actual_help_text = Model._meta.get_field(field).help_text
            self.assertEquals(
                help_text,
                actual_help_text,
                msg=f'\n   {field}: help_text'
            )
        
        if max_length is not None:
            actual_max_length = Model._meta.get_field(field).max_length
            self.assertEquals(
                max_length,
                actual_max_length,
                msg=f'\n   {field}: max_length'
            )
        
        actual_null = Model._meta.get_field(field).null
        self.assertEquals(
            null,
            actual_null,
            msg=f'\n   {field}: null'
        )
        
        actual_unique = Model._meta.get_field(field).unique
        self.assertEquals(
            unique,
            actual_unique,
            msg=f'\n   {field}: unique'
        )
        
        actual_verbose_name = Model._meta.get_field(field).verbose_name
        self.assertEquals(
            verbose_name, 
            actual_verbose_name,
            msg=f'\n   {field}: verbose_name'
        )

    
    # Test displays error for blank=False fields.
    def model_blank_field_error_test(self, data={}):
        required_fields = []
        Model = self.model()
        for field in Model._meta.fields:
            if field.blank is False:
                required_fields.append(field.name)

        for field, value in data.items():
            if field in required_fields:
                _data = {**data}
                _data[field] = ''
                
                with self.assertRaises(ValidationError):
                    Model.objects.create(**_data)
                self.assertEqual(Model.objects.count(), 0)

            
    def primary_key_test(self, pk_field, pk_test_value):
        Model = self.model()
        self.create()
        pk_dict = {}
        pk_dict[pk_field] = pk_test_value
        field_key = Model.objects.get(**pk_dict)
        primary_key = Model.objects.get(pk=pk_test_value)
        
        self.assertEquals(field_key, primary_key)
        
        
    def str_test(self, expected_string, **kwargs):
        Model = self.model()
        str_object = Model.objects.create(**kwargs)
        self.assertEqual(str(str_object), expected_string)

    
    def verbose_name_plural_test(self, plural_name):
        Model = self.model()
        self.assertEqual(str(Model._meta.verbose_name_plural), plural_name)