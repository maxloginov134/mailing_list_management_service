# Generated by Django 4.0.4 on 2023-07-19 19:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sending', '0002_sending'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sending',
            name='start_sending_date',
            field=models.DateField(default=datetime.datetime(2023, 7, 19, 22, 33, 13, 519053), verbose_name='Дата начала'),
        ),
        migrations.AlterField(
            model_name='sending',
            name='start_sending_time',
            field=models.TimeField(blank=True, default=datetime.time(22, 33, 13, 519053), null=True, verbose_name='время рассылки'),
        ),
        migrations.CreateModel(
            name='TrySending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_attempt', models.DateTimeField(auto_now_add=True, verbose_name='Дата последней попытки')),
                ('status_attempt', models.CharField(choices=[('success', 'завершена'), ('failure', 'провалена'), ('in_progress', 'в процессе')], default='in_progress', max_length=30, verbose_name='Текущий статус')),
                ('answer_server', models.CharField(max_length=20, verbose_name='Ответ почтового сервера')),
                ('sending', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sending.sending', verbose_name='Письмо')),
            ],
            options={
                'verbose_name': 'Попытка рассылки',
                'verbose_name_plural': 'Попытки рассылок',
            },
        ),
    ]
