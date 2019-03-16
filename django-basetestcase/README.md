BaseTestCase
============

BaseTestCase is a collection of cheater methods for the Django TestCase.
They are extensions of the Django TestCase.
These came about as a result of learning and using TDD.

There are four different classes:

    1. ModelTestCase
    2. FormTestCase
    3. ViewTestCase
    4. FunctionalTestCase
        - For use with Selenium.
        - Origins and some methods from "Obey The Testing Goat".


Quick start
-----------

Import into test and use:

    from basetestcase import ModelTestCase
    
    class ModelTest(ModelTestCase):
    
        ...