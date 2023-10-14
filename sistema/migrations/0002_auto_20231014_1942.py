# Generated by Django 3.2.22 on 2023-10-14 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estacionamiento',
            old_name='ubicacion',
            new_name='dirección',
        ),
        migrations.AddField(
            model_name='estacionamiento',
            name='comuna_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='sistema.comuna'),
            preserve_default=False,
        ),
    ]
