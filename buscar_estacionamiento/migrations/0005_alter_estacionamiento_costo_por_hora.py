# Generated by Django 3.2.22 on 2023-10-22 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buscar_estacionamiento', '0004_estacionamiento_costo_por_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacionamiento',
            name='costo_por_hora',
            field=models.IntegerField(default=0),
        ),
    ]
