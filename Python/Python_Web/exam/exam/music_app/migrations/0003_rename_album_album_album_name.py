# Generated by Django 4.0.2 on 2022-02-27 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0002_album_remove_profile_album_remove_profile_artist_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='album',
            new_name='album_name',
        ),
    ]
