# Generated by Django 2.0.2 on 2018-03-02 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20180302_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currencyvalue',
            name='date',
            field=models.DateTimeField(),
        ),
    ]