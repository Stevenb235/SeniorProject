# Generated by Django 5.0.3 on 2024-04-24 18:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 1, 18, 11, 56, 545504, tzinfo=datetime.timezone.utc)),
        ),
    ]
