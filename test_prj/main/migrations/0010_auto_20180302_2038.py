# Generated by Django 2.0.2 on 2018-03-02 18:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_currencyvalue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currencyvalue',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
