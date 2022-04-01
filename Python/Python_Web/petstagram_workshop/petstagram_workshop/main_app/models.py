from django.contrib.auth import get_user_model
from django.db import models

from petstagram_workshop.common.validators import ValidateFileMaxSizeInMb

UserModel = get_user_model()


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

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        unique_together = ('user', 'name')


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
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class Like(models.Model):
    photo = models.ForeignKey(
        PetPhoto,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
