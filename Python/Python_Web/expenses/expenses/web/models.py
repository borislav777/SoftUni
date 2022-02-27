from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from expenses.web.validators import validate_only_letters, ValidateFileMaxSizeInMb


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 15
    FIRST_NAME_MIN_LENGTH = 2

    LAST_NAME_MAX_LENGTH = 15
    LAST_NAME_MIN_LENGTH = 2

    BUDGET_DEFAULT = 0
    BUDGET_MIN_VALUE = 0

    PICTURE_UPLOAD_TO_DIR = 'profiles/'

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    budget = models.FloatField(
        default=BUDGET_DEFAULT,
        validators=(
            MinValueValidator(BUDGET_MIN_VALUE),
        )

    )

    profile_image = models.ImageField(
        null=True,
        blank=True,
        upload_to=PICTURE_UPLOAD_TO_DIR,
        validators=(
            ValidateFileMaxSizeInMb(5),
        )
    )

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class Expense(models.Model):
    TITLE_MAX_LENGTH = 30

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    expense_image = models.URLField()

    description = models.TextField(
        null=True,
        blank=True,
    )

    price = models.FloatField()
