
# UtilityTestCase
Has methods used both by [FormTestCase](https://github.com/Spleeding1/django-basetestcase/blob/master/django-basetestcase/FormTestCase.md) and [ViewTestCase](https://github.com/Spleeding1/django-basetestcase/blob/master/django-basetestcase/ViewTestCase.md)

- [formset_filler()](#formset_filler)
- [instances_saved_test()](#instances_saved_test)

## formset_filler()
Will generate `forms` to test `formsets`. Will also return all of<br />
the `instances` that were created to test all of them were saved<br />
in a `Model`. It appends the loop count to the end of the field.<br />
Greater functionality will come later.

```python
def formset_filler(self, field_data={}, initial=0, model=None,
    prefix='form', total=1)
```

- field_data: One `form`s worth of valid data. It uses this data and<br />
generates to fill the formset.
- initial: The number of `initial forms`. Generates these as well.
- model: If given, will `create` the `initial` instances in it.
- prefix: The name of the `prefix` intended to be used.
- total: The `TOTAL_FORMS` in the `formset`.

## instances_saved_test()
Will take a dictionary of dictionaries and loop through each one to<br />
test that the `instance` in saved in the `Model`.

```python
def instances_saved_test(self, model, instances, count=0)
```

- model: The model where the instances should be saves.
- instances: The dictionary of `instances`.
- count: Verifies that the total number of objects in the model is<br />
correct. Essentially, checks that updated instances were updated, not<br />
new ones created.

```python
view_data, instances_test_data = self.formset_filler(
    field_data={
        'field_1': 'This is field one.',
        'field_2': 'This is field two.',
    },
    prefix='my_prefix',
    model=MyModel,
    initial=2,
    total=4
)
response = self.client.post(reverse('my_reverse', view_data)
self.instances_saved_test(MyModel, instances_test_data, count=4)
```
