
# django-basetestcase
BaseTestCase is a collection of cheater methods for the Django TestCase. They are extensions of the Django TestCase. These came about as a result of learning and using TDD.

There are four different classes:
1. [ModelTestCase](https://github.com/Spleeding1/django-basetestcase/blob/master/django-basetestcase/ModelTestCase.md)
2. [FormTestCase](https://github.com/Spleeding1/django-basetestcase/blob/master/django-basetestcase/FormTestCase.md)
3. [ViewTestCase](https://github.com/Spleeding1/django-basetestcase/blob/master/django-basetestcase/ViewTestCase.md)
4. [FunctionalTestCase](https://github.com/Spleeding1/django-basetestcase/blob/master/django-basetestcase/FunctionalTestCase.md)
    - For use with Selenium.
    - Origins and some methods from "Obey The Testing Goat".
    
## Quickstart
To install:
`pip install django-basetestcase`

To use in a test:

`from basetestcase import ModelTestCase`

Please check out the [source code](https://github.com/Spleeding1/django-basetestcase/tree/master/django-basetestcase/basetestcase) for details. Documentation will be coming bit by bit. Any suggestions or issues, please let me know.

### Compatibility
This was built using Python 3.7 and Django 2.1.7. Anything prior to that has no guarantees.

### What's new?
Documentation has been added.
