from basetestcase import ModelTestCase

from _test_app.models import MyModel


class ModelTestCaseTest(ModelTestCase):
    
    def create(self, my_field):
        instance = MyModel.objects.create(my_field=my_field)
        return instance
    
    
    def model(self):
        return MyModel
    
    
    def test_fields(self):
        self.model_field_test(
            'my_field',
            help_text='This is help text.',
            max_length=255,
            unique=True,
            verbose_name='My Field:'
        )