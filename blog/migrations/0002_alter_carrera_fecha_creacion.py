# Generated by Django 5.0 on 2023-12-08 14:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrera',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 8, 11, 26, 27, 769471)),
        ),
    ]
