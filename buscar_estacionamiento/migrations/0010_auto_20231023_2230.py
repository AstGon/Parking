# Generated by Django 3.2.22 on 2023-10-24 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buscar_estacionamiento', '0009_auto_20231023_2222'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='username',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='dueno',
            old_name='username',
            new_name='email',
        ),
    ]