from django.core.validators import MinLengthValidator, RegexValidator, MinValueValidator
from django.db import models


class Profile(models.Model):
    USERNAME_MAX_LENGTH = 15
    USERNAME_MIN_LENGTH = 2

    AGE_MIN_VALUE = 0

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(USERNAME_MIN_LENGTH),
            RegexValidator(r'^[0-9a-zA-Z\_]*$', "Ensure this value contains only letters, numbers, and underscore."),
        )
    )

    email = models.EmailField()

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            MinValueValidator(AGE_MIN_VALUE),
        )
    )


class Album(models.Model):

    ALBUM_NAME_MAX_LENGTH = 30
    ARTIST_MAX_LENGTH = 30

    GENRE_MAX_LENGTH = 30
    POP_MUSIC = 'Pop Music'
    JAZZ_MUSIC = 'Jazz Music'
    R_B = "R&B Music"
    ROCK = "Rock Music"
    COUNTRY = "Country Music"
    DANCE = "Dance Music"
    HIPHOP = "Hip Hop Music"
    OTHER = "Other"
    GENRES = [POP_MUSIC, JAZZ_MUSIC, R_B, ROCK, COUNTRY, DANCE, HIPHOP, OTHER]
    CHOICES = [(x, x) for x in GENRES]

    PRICE_MIN_VALUE = 0.0

    album_name = models.CharField(
        unique=True,
        max_length=ALBUM_NAME_MAX_LENGTH,

    )

    artist = models.CharField(
        max_length=ARTIST_MAX_LENGTH,
    )

    genre = models.CharField(
        max_length=GENRE_MAX_LENGTH,
        choices=CHOICES,

    )
    description = models.TextField(
        blank=True,
        null=True,
    )

    image_url = models.URLField()

    price = models.FloatField(
        validators=(
            MinValueValidator(PRICE_MIN_VALUE),
        )
    )
