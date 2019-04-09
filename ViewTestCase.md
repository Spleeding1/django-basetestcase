
# ViewTestCase
```python
from basetestcase import ViewTestCase
```
- [Test class setup](#Test-class-setup)
- [AJAX](#AJAX)
- [assertTemplatesUsed()](#assertTemplatesUsed)
- [path_to_correct_view_test()](#path_to_correct_view_test)
- [view_required_field_error_test()](#view_required_field_error_test)
- [formset_filler() and instances_saved_test()](#formset_filler-and-instances_saved_test)

```python
from django.shortcuts import render

from .forms import MyForm, MyFormSet
from .models import MyModel

def my_form_view(request):
    my_form = MyForm()
    return render(request, 'my_template.html', {'form': my_form})

def my_formset_view(request):
    my_formset = MyFormSet()
    return render(request, 'my_template.html', {'formset': my_formset})
```

## Test class setup
There is a required method as a part of using this test class.

```python
def POST(self, data={'field_1': 'This is field one.', 'field_2': 'This is field two.'}):
    return self.client.post(reverse('my_reverse'), data)
```

## AJAX
Used to test views with `request.is_ajax()`.

```python
AJAX = {'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}
```

```python
from basetestcase import AJAX

...
self.client.post(reverse('my:reverse'), data, **AJAX)
```

## assertTemplatesUsed()
An extension of `assertTemplateUsed` to assert more than one `template`.

```python
def assertTemplatesUsed(self, response, *templates)
```
- response: `self.client.foo(bar)`
- templates: All of the `templates` used in the `response`.

```python
response = self.client.get(reverse('my:reverse'))
self.assertTemplatesUsed(response, 'my_template_1.html', 'my_template_2.html')
```

## path_to_correct_view_test()
Tests `path` `url` and `name` `resolve` to the correct `view`.<br />
(I have not tested this with `class` based views.)

```python
def path_to_correct_view_test(self, view, url=None, name=None, args=None)
```
- url: The complete url path.
- name: The url `reverse` name.
- args: args needed for `reverse`.

```python
# Given this path:
path('my_view/<int:pk>/', views.my_view, name='my_view')

# This is the test:
self.path_to_correct_view_test(
    my_view,
    url='/my_view/1/',
    name='my_view',
    args=1
)
```

## view_required_field_error_test()
Takes a dictionary of the required values of the `view` and
loops through them setting each one to a empty string, testing
each loop for `'This field is required'`.

```python
def view_required_field_error_test(self, required_fields=[])
```
- data: A dictionary with a valid value for each `required` field.
- required_fields: A list of all of the fields that are `required`.

```python
self.view_required_field_error_test(
    data={
        'field_1': 'This is field one.',
        'field_2': 'This is field two.',
    },
    required_fields=['field_1', 'field_2']
)
```

## formset_filler() and instances_saved_test()
Both [formset_filler()](https://github.com/Spleeding1/django-basetestcase/blob/master/UtilityTestCase.md) and [instances_saved_test()](https://github.com/Spleeding1/django-basetestcase/blob/master/UtilityTestCase.md) methods are accessible in the `ViewTestCase`.
