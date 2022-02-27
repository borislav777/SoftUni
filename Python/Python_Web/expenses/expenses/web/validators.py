from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

VALIDATE_ONLY_LETTERS_EXX_ERROR = "Ensure this value contains only letters."


def validate_only_letters(value):
    if not value.isalpha():
        raise ValidationError(VALIDATE_ONLY_LETTERS_EXX_ERROR)


@deconstructible
class ValidateFileMaxSizeInMb:

    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self._megabytes_to_bytes(self.max_size):
            raise ValidationError(self._get_exception_message())

    @staticmethod
    def _megabytes_to_bytes(value):
        return value * 1024 * 1024

    def _get_exception_message(self):
        return f"Max file size is {self.max_size:.2f} MB"
