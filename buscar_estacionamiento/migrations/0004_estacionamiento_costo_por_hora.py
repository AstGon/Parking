# Generated by Django 3.2.22 on 2023-10-22 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buscar_estacionamiento', '0003_remove_estacionamiento_capacidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='estacionamiento',
            name='costo_por_hora',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
