# Generated by Django 4.0.2 on 2022-02-04 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_petphoto_date_and_time_publication_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petphoto',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
    ]
