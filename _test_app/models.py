from django.db import models


class MyModel(models.Model):
    
    my_field = models.CharField(
        'My Field:',
        help_text='This is help text.',
        max_length=255,
        unique=True
    )