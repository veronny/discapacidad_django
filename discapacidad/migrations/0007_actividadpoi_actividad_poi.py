# Generated by Django 5.0.4 on 2024-06-24 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discapacidad', '0006_actividadpoi_programacionmensual_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividadpoi',
            name='actividad_poi',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
