
# FunctionalTestCase
```python
from basetestcase import FunctionalTestCase
```

[Test class setup](#Test-class-setup)<br />
[Locating Elements](#Locating-Elements)<br />
[WebElement Methods](#WebElement-Methods)<br />

Methods:
- [element_has_focus()](#element_has_focus())
- [get_body()](#get_body())
- [get_button_test()](#get_button_test())
- [get_checkbox_test()](#get_checkbox_test())
- [get_content_header_test()](#get_content_header_test())
- [get_form_control_input_box_test()](#get_form_control_input_box_test())
- [get_nabar()](#get_navbar())
- [get_page()](#get_page())
- [hover()](#hover())
- [setUp()](#setUp())
- [sleep()](#sleep())
- [tearDown()](#tearDown)
- [wait_for()](#wait_for())
- [wait_for_error_test()](#wait_for_error_test())
- [wait_for_form_submission_test()](#wait_for_form_submission_test())
- [wait_for_invalid()](#wait_for_invalid())
- [wait_for_valid()](#wait_for_valid())

## Test class setup
This test class started with [Obey the Testing Goat](http://www.obeythetestinggoat.com/pages/book.html).<br />
The `driver` is called as `self.browser`.<br />
If you change this, things will not work correctly.

## Locating Elements
Shortcuts, as opposed to `self.browser.find_element_by_id()`.

- self.find_class('my_class')
- self.find_id('my_element_id')
- self.find_selector('my_css_selector')
- self.find_xpath('my_xpath')

## element_has_focus()
Tests if the current active element is the desired active element.

```python
def element_has_focus(self, element)
```

- element: The element that is supposed to have focus.

```python
self.element_has_focus(self.find_id('id_my_element'))
```

## get_body()
Gets the body of the page.

```python
def get_body(self)
```

## get_button_test()
Tests a button and returns the button element.

```python
def get_button_test(self, button_id, button_text='', css_class='btn btn-main button-main btn-block',
    is_below=None, is_to_the_right_of=None, _type='submit')
```

- button_id: The id of the button.
- button_text: Tests the text of the button.
- css_class: Tests the css class of the button.
- is_below: Tests that the button's `location[y]` is greater<br />
than the given element.
- is_to_the_right_of: Tests that the button's `location[x]`<br />
is greater than the given element.
- _type: Tests the button type.

```python
my_button = self.get_button_test(
   'myButton',
    button_text='My Button',
    is_below=self.find_id('id_above')
)
```

## get_checkbox_test()
Tests a checkbox and returns the checkbox element.

```python
def get_checkbox_test(self, checkbox_id, checked=False, css_class='',
    is_below=None, label=None)
```

- checkbox_id: The id of the checkbox.
- checked: Tests if the checkbox is checked.
- css_class: Tests the css class of the checkbox.
- is_below: Tests that the checkboxs's `location[y]` is greater<br />
than the given element.
- label: If given, will test the label text, and that the<br />
checkbox is nested inside the label tag.

```python
checkbox = self.get_checkbox_test(
    'id_checkbox',
    checked=True,
    css_class='checkbox-class',
    is_below=self.find_id('id_above'),
    label='My Label'
)
```

## get_content_header_test()
I was using a `content-header`class in my layout. This is the way<br />
I started testing for them. `return`s the header element.

```python
def get_content_header_test(self, header_text, is_below=None, number=1)
```

- header_text: Tests the text of the header.
- is_below: Tests that the header's `location[y]` is greater<br />
than the given element.
- number: The number of the header on the page.

## get_form_control_input_box_test()
Tests an input box and returns the input box element.<br />
If `help_text` is given, returns both elements.

```python
def get_form_control_input_box_test(self, box_id, css_class='form-control',
    help_text=None, help_text_css_class='help-text text-muted', is_below=None,
    label=None, placeholder='', value='')
```

- box_id: The id of the box.
- css_class: Tests the css class of the box.
- help_text: If given, tests the `help_text` for the box.<br />
If none is given, tests that `help_text` does not exist.<br />
**Note:** *The help_text is located by `id` in this format:*<br />
    `box_help_text = self.browser.find_xpath(f'//small[@id="{box_id}_help_text"]')`
- help_text_css_class: Tests the css_class of the `help_text`.
- is_below: Tests that the box's `location[y]` is greater<br />
than the given element.
- label: Test the label of the box. If none is given, tests<br />
that none exists.
- placeholder: Tests the placeholder of the box.
- value: Tests the value of the box.

```python
box, help_text = self.get_form_control_input_box_test(
    'id_input_box',
    help_text='I am help text',
    is_below=above_element,
    placeholder='I am a placeholder',
)
```

## get_navbar
Finds and returns the element with the `tag_name` `<nav>`.

```python
self.get_navbar()
```

## get_page
Get the page `url` and sets window size.

```python
def get_page(self, url_extention, window=None)
```

- url_extension: The page path.
- window: Sets window size, either `'xs', 'sm', 'md', 'lg', 'xl'`.<br />
Default is `'xs'`

```python
self.get_page('/this-is/my-url', window='md')
```

## hover()
Hovers mouse over element.

```python
def hover(self, element)
```

- element: The element to hover over.

## setUp()
I'm just going to list it all here. [staging_server](http://www.obeythetestinggoat.com/book/chapter_manual_deployment.html)

```python
def setUp(self):
    self.browser = webdriver.Chrome()
    staging_server = os.environ.get('STAGING_SERVER')
    
    if staging_server:
        self.live_server_url = 'http://' + staging_server
```

## sleep()
Uses `time.sleep()`.

```python
def sleep(self, n)
```

- n: The desired sleep time.

```python
self.sleep(30)
```

## tearDown()
Closes browser window.

```python
def tearDown(self):
        self.browser.quit()
```

## wait_for()
Waits a set time before raising an `error`. [@wait](http://www.obeythetestinggoat.com/book/chapter_fixtures_and_wait_decorator.html)

```python
self.wait_for(lambda: self.find_id('id_my_input'))
```

## wait_for_error_test()
Tests for an error message displayed on a page.<br />
Uses the [`wait_for`](#wait_for()) method.

```python
def wait_for_error_test(self, error_message, css_class='alert alert-danger d-flex justify-content-center rounded',
    find=('class', 'alert'), is_above=None, is_below=None)
```

- error_message: Tests the text of the error message.
- css_class: Tests the css class of the error.
- find: Uses a `tuple` to locate the error.<br />
Can be either `'class'` or `'xpath'`.
- is_above: Tests that the error's `location[y]` is less<br />
than the given element.
- is_below: Tests that the error's `location[y]` is greater<br />
than the given element.

## wait_for_form_submission_test()
Tests for submitted information to be displayed on the success page.<br />
Uses the [`wait_for`](#wait_for()) method.

```python
def wait_for_form_submission_test(self, *data, element=None)
```

- data_list: The information that should be displayed after form submission.
- element: the element where the information should be found.<br />
If `None` is given, `body` is the default.

```python
self.wait_for_form_submission_test(
    'I',
    'was',
    'submitted',
    'by a form.'
)
```

## wait_for_invalid()
Waits for element to be `:invalid`.

```python
self.wait_for_invalid('element_id')
```

## wait_for_valid()
Waits for element to be `:valid`.

```python
self.wait_for_valid('element_id')
```

# WebElement Methods
These are "monkey patched" methods.

```python
WebElement.method = WebElement_method
```

- [WebElement_has_placeholder()](#WebElement_has_placeholder())
- [WebElement_has_value()](#WebElement_has_value())
- [WebElement_is_above()](#WebElement_is_above())
- [WebElement_is_below()](#WebElement_is_below())
- [WebElement_is_between()](#WebElement_is_between())
- [WebElement_is_help_text()](#WebElement_is_help_text())
- [WebElement_is_label()](#WebElement_is_label())
- [WebElement_is_to_the_right_of()](#WebElement_is_to_the_right_of())
- [WebElement_uses_css_class()](#WebElement_uses_css_class())

## WebElement_has_placeholder()
Tests the placeholder of an element.

```python
my_element.has_placeholder('placeholder')
```

## WebElement_has_value()
Tests the value of an element.

```python
my_element.has_value('value')
```

## WebElement_is_above()
Tests that the element's `location[y]` is less<br />
than the given element.

```python
my_element.is_above(below_element)
```

## WebElement_is_below()
Tests that the element's `location[y]` is greater<br />
than the given element.

```python
my_element.is_below(above_element)
```

## WebElement_is_between()
Tests that the element's `location[y]` is greater<br />
than the above element and less than the below_element.

```python
my_element.is_between(above_element, below_element)
```

## WebElement_is_help_text()
Tests if element is help_text.

```python
WebElement_is_help_text(self, help_text,
    css_class='help-text text-muted', is_below=None)
```

- css_class: Tests the css class of the help_text.
- help_text: Tests the text.

```python
my_element.is_help_text(
    'I am help text.',
    is_below=above_element
)
```

## WebElement_is_label()
Test if element is a label.

```python
def WebElement_is_label(self, label, is_above=None, is_below=None):
```

- is_above: Tests that the label's `location[y]` is less<br />
than the given element.
- is_below: Tests that the label's `location[y]` is greater<br />
than the given element.
- label: Tests the label text.

```python
my_element.is_label(
    'My Label:',
    is_above=my_input_box,
    is_below=above_element
)
```

## WebElement_is_to_the_right_of()
Tests that the element's `location[x]` is greater<br />
than the given element.

```python
my_element.is_to_the_right_of(left_element)
```

## WebElement_uses_css_class()
Tests the elements class attribute is equal to the given class.

```python
my_element.uses_css_class('these are classes')
```
