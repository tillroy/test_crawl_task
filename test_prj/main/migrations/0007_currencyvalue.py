# Generated by Django 2.0.2 on 2018-03-02 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_delete_currencyvalue'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(max_length=10)),
                ('correlation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.CurrencyСorrelation')),
            ],
        ),
    ]
