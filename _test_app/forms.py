from django.forms import BaseModelFormSet, ModelForm, modelformset_factory

from _test_app.models import MyModel


class MyForm(ModelForm):
    
    class Meta:
        model = MyModel
        fields = ['my_field']


class MyBaseFormSet(BaseModelFormSet):
    
    def clean(self):
        return super().clean()


MyFormSet = modelformset_factory(
    MyModel,
    form=MyForm,
    formset=MyBaseFormSet
)