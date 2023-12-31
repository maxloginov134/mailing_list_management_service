# Generated by Django 4.0.4 on 2023-07-20 16:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sending', '0003_alter_sending_start_sending_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sending',
            name='start_sending_date',
            field=models.DateField(default=datetime.datetime(2023, 7, 20, 19, 3, 17, 980858), verbose_name='Дата начала'),
        ),
        migrations.AlterField(
            model_name='sending',
            name='start_sending_time',
            field=models.TimeField(blank=True, default=datetime.time(19, 3, 17, 980857), null=True, verbose_name='время рассылки'),
        ),
    ]
