# Generated by Django 3.2.22 on 2023-10-25 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buscar_estacionamiento', '0002_alter_customuser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
