# Generated by Django 5.0 on 2023-12-05 15:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('description', models.CharField(blank=True, max_length=120)),
                ('quantity', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0, message='Quantity must be at least 0.'), django.core.validators.MaxValueValidator(100, message='Quantity must be at most 100.')])),
            ],
        ),
    ]
