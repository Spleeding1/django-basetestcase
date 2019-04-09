from basetestcase import FormTestCase

from _test_app.forms import MyForm, MyBaseFormSet, MyFormSet
from _test_app.models import MyModel


class FormTestCaseTest(FormTestCase):
    
    def form(self, *args, **kwargs):
        form = MyForm(*args, **kwargs)
        return form
    
    
    def test_field_rendered(self):
        self.form_field_test(
            'my_field',
            help_text='This is help text.',
            label='My Field:',
            widget_attrs={'maxlength': '255'}
        )
    
    
    def test_MyFormSet(self):
        formset = MyFormSet()
        self.formset_test(
            baseformset=MyBaseFormSet,
            field_data={'my_field': 'My Field'},
            form=MyForm,
            formset=MyFormSet,
        )