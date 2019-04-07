from django.test import TestCase


class UtilityTestCase(TestCase):
    
    def formset_filler(self, field_data={}, initial=0, model=None, prefix='form', total=1):
        form_data = {}
        form_data[f'{prefix}-INITIAL_FORMS'] = str(initial)
        form_data[f'{prefix}-TOTAL_FORMS'] = str(total)
        for i in range(initial):
            model_instance = {}
            for field,value in field_data.items():
                model_instance[field] = f'{value}{(i + total)}'
            model.objects.create(**model_instance)
        test_model_instances = {}
        for i in range(total):
            test_model_instance = {}
            for field,value in field_data.items():
                new_value = f'{value}{i}'
                form_data[f'{prefix}-{i}-{field}'] = new_value
                if i < initial:
                    form_data[f'{prefix}-{i}-id'] = (i + 1)
                test_model_instance[field] = new_value
            test_model_instances[str(i)] = test_model_instance
        return form_data, test_model_instances
        
    
    def instances_saved_test(self, model, instances, count=0):
        for i in instances:
            self.assertTrue(model.objects.filter(**instances[i]).exists())
            self.assertEqual(model.objects.count(), count)