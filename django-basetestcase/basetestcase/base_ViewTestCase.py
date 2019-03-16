from django.test import TestCase
from django.urls import resolve, reverse


AJAX = {'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}


class ViewTestCase(TestCase):
    
    def name_to_correct_view_test(self, view_name, view, args=None):
        if args is not None:
            name = resolve(reverse(view_name, args=[args]))
        else:
            name = resolve(reverse(view_name))
        
            self.assertEqual(name.func, view)


    def url_to_correct_view_test(self, view_url, view):
        url = resolve(view_url)
        
        self.assertEqual(url.func, view)


    def view_required_field_error_test(self, dictionary, required_fields=[]):
        _dict = dict(dictionary)

        for field, value in _dict.items():
            if field in required_fields:
                original_value = value
                _dict[field] = ''
                response = self.post(_dict)
            
                self.assertContains(
                    response,
                    'This field is required.',
                    msg_prefix=f'{field}'
                )
                    
                _dict[field] = original_value
    
    
    def view_uses_correct_templates_test(self, view_name, *templates, args=None, ajax=False):
        if ajax is not False and args is not None:
            response = self.client.get(
                reverse(view_name, args=[args]),
                **AJAX
            )
        elif ajax is not False:
            response = self.client.get(
                reverse(view_name), **AJAX)
        elif args is not None:
            response = self.client.get(
                reverse(view_name, args=[args])
            )
        else:
            response = self.client.get(reverse(view_name))
        for t in templates:
          self.assertTemplateUsed(response, t)