from django.core.validators import MinLengthValidator
from django.db import models

from petstagram_workshop.main_app.validators import validate_only_letters_use,ValidateFileMaxSizeInMb


class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30

    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'

    GENDERS = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letters_use,
        )
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_letters_use,
        )
    )

    picture = models.URLField()

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    email = models.EmailField(
        blank=True,
        null=True,
    )

    gender = models.CharField(
        max_length=max(len(x) for x, _ in GENDERS),
        choices=GENDERS,
        blank=True,


    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Pet(models.Model):
    NAME_MAX_LENGTH = 30

    CAT = "Cat"
    DOG = "Dog"
    BUNNY = "Bunny"
    PARROT = "Parrot"
    FISH = "Fish"
    OTHER = "Other"
    TYPE = [(x, x) for x in (CAT, DOG, BUNNY, PARROT, FISH, OTHER)]

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,

    )

    type = models.CharField(
        max_length=max(len(x) for x, _ in TYPE),
        choices=TYPE,

    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        unique_together = ('user_profile', 'name')


class PetPhoto(models.Model):
    photo = models.ImageField(
        upload_to='profile',
        validators=(
            ValidateFileMaxSizeInMb(5),
        ),
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    date_and_time_publication = models.DateTimeField(
        auto_now_add=True,
    )

    likes = models.IntegerField(
        default=0,
    )

    tagged_pets = models.ManyToManyField(
        Pet,


    )
