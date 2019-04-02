from .base_UtilityTestCase import UtilityTestCase
from django.urls import resolve, reverse


AJAX = {'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}


class ViewTestCase(UtilityTestCase):
    
    def assertTemplatesUsed(self, response, *templates):
        for t in templates:
            self.assertTemplateUsed(response, t)
    
    
    def path_to_correct_view_test(self, view, url=None, name=None, args=None):
        if name is None and url is None:
            self.fail('No name or url has been entered')
        
        if url is not None:
            _url = resolve(url)
            self.assertEqual(_url.func, view)
        
        if name is not None:
            if args is not None:
                _name = resolve(reverse(name, args=[args]))
            else:
                _name = resolve(reverse(name))
            self.assertEqual(_name.func, view)
            

    def view_required_field_error_test(self, data, required_fields=[]):
        _data = dict(data)

        for field, value in _data.items():
            if field in required_fields:
                original_value = value
                _data[field] = ''
                response = self.post(_data)
            
                self.assertContains(
                    response,
                    'This field is required.',
                    msg_prefix=f'{field}'
                )
                    
                _data[field] = original_value