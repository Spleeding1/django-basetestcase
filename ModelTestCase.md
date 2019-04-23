
# ModelBaseTest
```python
from basetestcase import ModelTestCase
```

- [Test class setup](#Test-class-setup)
- [model_field_test()](#model_field_test)
- [model_blank_field_error_test()](#model_blank_field_error_test)
- [primary_key_test()](#primary_key_test)
- [str_test()](#str_test)
- [verbose_name_plural_test()](#verbose_name_plural_test)

```python
from django.db import models

class MyModel(models.Model):
    my_charfield = models.CharField(
        'My CharField',
        blank=True,
        default='Default',
        error_messages={'unique': 'This field is unique.'}
        help_text='This is help text.',
        max_length=100,
        unique=True
    )
    field_1 = models.Charfield(
        'Field 1',
        max_length=50
    )
    field_2 = models.Charfield(
        'Field 2',
        max_length=75
    )
    
    class Meta:
        verbose_name_plural = 'Plural Model'
    
    def __str__(self):
        return self.field_1
```

# Test class setup
There are two methods requires as a part of using this test class.

```python
class MyModelTest(ModelTestCase):
    
    def model(self):
        return MyModel
    
    def create(self):
        my_instance = MyModel.objects.create(
            field_1='This is field one.',
            field_2='This is field two.',
            my_charfield='I am not required.'
        )
```

## model_field_test()
Tests the setup of a `Model`'s field.

```python
def model_field_test(self, field, blank=False, choices=None,
    default=None, error_messages=None, help_text=None,
    max_length=None, null=False, primary_key=False,
    unique=False, verbose_name='')
```

- field: A string of the Model's field name.
- blank: Tests if field's `blank` is set to `True` or `False`.
- choices: Tests the `choices` set on the field.
- default: Tests the `default` value.
- error_messages: A dictionary of the `error_messages`.
- help_text: Tests the `help_text` set on the field.
- null: Tests if field's `null` is set to `True` or `False`.
- primary_key: Tests if field's `primary_key` is set to `True` or `False`.
- unique: Tests if field `is unique`.
- verbose_name: Tests field's `verbose_name`.

```python
self.model_field_test(
    'my_charfield',
    blank=True,
    default='Default',
    error_messages={'unique': 'This field is unique.'},
    help_text='This is help text.'
    unique=True,
    verbose_name='My CharField'
)
```

## model_blank_field_error_test()
Takes a dictionary of the required values of the `Model` and
loops through them setting each one to a empty string, testing
each loop for a `ValidationError` and the `Model.objects.count() == 0`.
 
```python
def model_blank_field_error_test(self, data={})
```

- data: A dictionary with a valid value for each `blank=False` field.

```python
self.model_blank_field_error_test(
    data = {
        'field_1': 'This is field one.',
        'field_2': 'This is field two.',
})
```

## primary_key_test()
Creates an `instance` and tests that the set `primary_key` field<br />
and the desired `primary_key` field return the same `instance`.

```python
def primary_key_test(self, pk_field, pk_test_value)
```

- pk_field: The desired `primary_key` field.
- pk_test_value: The value use to get the `instance`.

```python
# if field_1 has primary_key=True
self.primary_key_test('field_1', 'This is field one.')
```

## str_test()
Tests the expected string for a `Model` `instance`.

```python
def str_test(self, expected_string, **kwargs)
```

- expected_string: The string that is expected for the instance.
- **kwargs: The data to make the instance.

```python
self.str_test(
    'This is field one.',
    field_1='This is field one.',
    field_2='This is field two.'
)
```

## verbose_name_plural_test()
Tests the `verbose_name_plural` set in the `Model`'s `Meta`.

```python
def verbose_name_plural_test(self, plural_name)
```

- plural_name: The expected plural string.

```python
self.verbose_name_plural_test('Plural Model')
```
