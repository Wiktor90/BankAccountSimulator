# Generated by Django 3.1.7 on 2021-02-24 09:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='created_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
