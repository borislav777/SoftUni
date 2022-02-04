from django.core.exceptions import ValidationError


def validate_only_letters_use(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Value must contain only letters')


def validate_file_max_size_in_mb(max_size):
    def validate(value):
        filesize = value.file.size
        if filesize > max_size * 1024 * 1024:
            raise ValidationError('Max file size is %sMB' % str(max_size))

    return validate
