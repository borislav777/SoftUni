# Generated by Django 4.0.2 on 2022-02-26 11:53

import django.core.validators
from django.db import migrations, models
import expenses.web.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('expense_image', models.URLField()),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), expenses.web.validators.validate_only_letters])),
                ('last_name', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), expenses.web.validators.validate_only_letters])),
                ('budget', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profiles/', validators=[expenses.web.validators.ValidateFileMaxSizeInMb(5)])),
            ],
        ),
    ]
