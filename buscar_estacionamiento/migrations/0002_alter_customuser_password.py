# Generated by Django 3.2.22 on 2023-10-25 16:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buscar_estacionamiento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=128, validators=[django.core.validators.MinLengthValidator(limit_value=8)]),
        ),
    ]
