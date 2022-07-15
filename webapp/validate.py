from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible


def validate_title(value):
    if len(value) > 15:
        raise ValidationError('Summary must be less 10 symbol')
    return value

@deconstructible
class MinLengthValidator(BaseValidator):
    massage = 'Value "%(value)s"has length of %(show_value)d! It should be at least %(limit_value)d symbols long! '
    code = 'too_short'

    def compare(self, a, b):
        return a < b

    def clean(self, x):
        return len(x)


