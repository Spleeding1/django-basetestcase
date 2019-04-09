import os
import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement


MAX_WAIT = 5


class FunctionalTestCase(StaticLiveServerTestCase):
    
    ''' Set "base_url = self.browser.current_url" '''
    def correct_link_url(self, link_text, base_url_extension):
        link = self.browser.find_element_by_link_text(
            link_text).click()
        link_url = self.browser.current_url
        
        self.assertEqual(link_url, self.base_url + base_url_extension)
        
        
    def correct_link_url_xs(self, link_text, base_url_extension):
        menu_icon = self.browser.find_element_by_class_name(
            'navbar-toggler')
        menu_icon.click()
        link = self.browser.find_element_by_link_text(
            link_text).click()
        link_url = self.browser.current_url
        
        self.assertEqual(
            link_url,
            self.base_url + base_url_extension
        )
        
        
    def element_has_focus(self, element):
        focus = self.browser.switch_to.active_element
        focus_id = focus.get_attribute('id')
        element_id = element.get_attribute('id')
        
        assert focus == element, f'{focus_id} != {element_id}'
        

    def get_body(self):
        return self.browser.find_element_by_tag_name('body')
    
    
    def get_button_test(self, button_id, button_text='', css_class='btn btn-main button-main btn-block', is_below=None, is_to_the_right_of=None, _type='submit', attrs={}):
        button = self.find_id(button_id)
        self.assertEqual(button.text, button_text)
        button.uses_css_class(css_class)
        if is_below is not None:
            button.is_below(is_below)
        if is_to_the_right_of is not None:
            button.is_to_the_right_of(is_to_the_right_of)
        self.assertEqual(button.get_attribute('type'), _type)
        for key,value in attrs.items():
            self.assertEquatl(button.get_attribute(key), value)
        return button
    
    
    def get_checkbox_test(self, checkbox_id, checked=False, css_class='', is_below=None, label=None):
        checkbox = self.find_id(checkbox_id)
        checkbox.uses_css_class(css_class)
        checkbox.is_below(is_below)
        self.assertEqual(checkbox.is_selected(), checked)
        checkbox_label = self.find_xpath(f'//label[@for="{checkbox_id}"]')
        checkbox_label.is_label(label)
        xpath_box = self.find_xpath(f'//label[@for="{checkbox_id}"]/input')
        self.assertEqual(
            checkbox.get_attribute('id'),
            xpath_box.get_attribute('id')
        )
        return checkbox
    
    
    def get_content_header_test(self, header_text, is_below=None, number=1):
        header = self.find_xpath(
            f'//div[@class="content-header"][{str(number)}]'
        )
        self.assertEqual(header.text, header_text)
        header.uses_css_class('content-header')
        if is_below is not None:
            header.is_below(is_below)
        return header
    
    
    def get_error_test(self, error_message, css_class='alert alert-danger d-flex justify-content-center rounded', find_class='alert', find_xpath=None, is_above=None, is_below=None):
        if find_xpath is None:
            error = self.find_class(find_class)
        else:
            error = self.find_xpath(find_xpath)
        self.assertEquals(error.text, error_message)
        error.uses_css_class(css_class)
        if is_above is not None:
            error.is_above(is_above)
        if is_below is not None:
            error.is_below(is_below)
        return error
    
    
    def get_form_control_input_box_test(self, box_id, css_class='form-control', help_text=None, help_text_css_class='help-text text-muted', is_below=None, label=None, placeholder='', value=''):
        box_label = is_below
        if label is not None:
            box_label = self.find_xpath(f'//label[@for="{box_id}"]')
            box_label.is_label(label, is_below=is_below)
        else:
            with self.assertRaises(NoSuchElementException):
                self.find_xpath(f'//label[@for="{box_id}"]')
        box = self.find_id(box_id)
        box.has_placeholder(placeholder)
        box.has_value(value)
        box.uses_css_class(css_class)
        
        if box_label is not None:
            box.is_below(box_label)
        if help_text is not None:
            box_help_text = self.find_xpath(
                f'//small[@id="{box_id}_help_text"]'
            )
            box_help_text.is_help_text(
                help_text,
                css_class=help_text_css_class,
                is_below=box
            )
            return box, box_help_text
        else:
            with self.assertRaises(NoSuchElementException):
                self.find_xpath(
                    f'//small[@id="{box_id}_help_text"]'
                )
        return box
    
    
    def get_navbar(self):
        return self.browser.find_element_by_tag_name('nav')

        
    def get_page(self, url_extention, window=None):
        window_size = [500, 700]
        if window == 'xs':
            window_size = [500, 700]
        elif window == 'sm':
            window_size = [700, 500]
        elif window == 'md':
            window_size = [900, 700]
        elif window == 'lg':
            window_size = [1024, 768]
        elif window == 'xl':
            window_size = [1400, 800]
            
        return (
            self.browser.get(self.live_server_url + url_extention),
            self.browser.set_window_size(window_size[0], window_size[1])
        )
        
        
    def hover(self, element):
        return ActionChains(self.browser
            ).move_to_element(element).perform()
        

    def setUp(self):
        self.browser = webdriver.Chrome()
        staging_server = os.environ.get('STAGING_SERVER')
        
        if staging_server:
            self.live_server_url = 'http://' + staging_server

    
    def sleep(self, n):
        return time.sleep(n)
      
      
    def tearDown(self):
        self.browser.quit()
        
        
    def wait(fn):  
        def modified_fn(*args, **kwargs):  
            start_time = time.time()
            while True:  
                try:
                    return fn(*args, **kwargs)  
                except (AssertionError, WebDriverException) as e:  
                    if time.time() - start_time > MAX_WAIT:
                        raise e
                time.sleep(0.5)
        return modified_fn
    
    
    @wait
    def find_class(self, css_class):
        element = self.browser.find_element_by_class_name(css_class)
        return element
    
    
    @wait
    def find_id(self, _id):
        element = self.browser.find_element_by_id(_id)
        return element
    
    
    @wait
    def find_selector(self, selector):
        element = self.browser.find_element_by_css_selector(selector)
        return element
    
    
    @wait
    def find_xpath(self, xpath):
        element = self.browser.find_element_by_xpath(xpath)
        return element
    
    
    @wait
    def wait_for(self, fn):
        return fn()
    
    
    @wait
    def wait_for_form_submission_test(self, *data, element=None):
        if element is None:
            element = self.get_body()
        for item in data:
            self.assertIn(item, element.text, msg=f'{item}')
    
    
    @wait
    def wait_for_invalid(self, element_id):
        element = self.find_selector(element_id + ':invalid')
        return element
    
    
    @wait
    def wait_for_valid(self, element_id):
        element = self.find_selector(element_id + ':valid')
        return element
    
        
    def WebElement_has_placeholder(self, placeholder):
        set_placeholder = self.get_attribute('placeholder') 
        assert set_placeholder == placeholder, f"\n{set_placeholder} !=\n{placeholder}"
        
    WebElement.has_placeholder = WebElement_has_placeholder
    
    
    def WebElement_has_value(self, value):
        set_value = self.get_attribute('value')
        assert set_value == value, f"\n{set_value} !=\n{value}"
        
    WebElement.has_value = WebElement_has_value
    
    
    def WebElement_is_above(self, below_element):
        above = self.location['y']
        below = below_element.location['y']
        assert above < below, f'"{above}"  > "{below}"'
        
    WebElement.is_above = WebElement_is_above
    
    
    def WebElement_is_below(self, above_element):
        below = self.location['y']
        above = above_element.location['y']
        assert above < below, f'"{above}"  > "{below}"'
        
    WebElement.is_below = WebElement_is_below
    
    
    def WebElement_is_between(self, above_element, below_element):
        self.is_below(above_element)
        self.is_above(below_element)
        
    WebElement.is_between = WebElement_is_between
        
        
    def WebElement_is_help_text(self, help_text, css_class='help-text text-muted', is_below=None):
        self.uses_css_class(css_class)
        assert self.text == help_text, f'\n"{self.text}" !=\n"{help_text}"'
        
        if is_below is not None:
            self.is_below(is_below)
            
    WebElement.is_help_text = WebElement_is_help_text
    
    
    def WebElement_is_label(self, label, is_above=None, is_below=None):
        assert label == self.text, f'\n"{label}" !=\n"{self.text}"'
        
        if is_above is not None:
            self.is_above(is_above)
        
        if is_below is not None:
            self.is_below(is_below)
            
    WebElement.is_label = WebElement_is_label
    
    
    def WebElement_is_to_the_right_of(self, left_element):
        right = self.location['x']
        left = left_element.location['x']
        assert left < right, f'"{left}" > "{right}"'
            
    WebElement.is_to_the_right_of = WebElement_is_to_the_right_of
    
    
    def WebElement_uses_css_class(self, css_class):
        element_css = self.get_attribute('class')
        assert css_class == element_css, f'\n"{css_class}" !=\n"{element_css}"'
            
    WebElement.uses_css_class = WebElement_uses_css_class