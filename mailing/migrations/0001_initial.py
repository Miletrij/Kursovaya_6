# Generated by Django 5.0.6 on 2024-06-29 15:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recipient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailingMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Содержание письма')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.CreateModel(
            name='MailingSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Начало рассылки')),
                ('end_time', models.DateTimeField(verbose_name='Конец рассылки')),
                ('sending_period', models.CharField(choices=[('daily', 'раз в день'), ('weekly', 'раз в неделю'), ('monthly', 'раз в месяц')], max_length=50, verbose_name='Период рассылки')),
                ('sending_status', models.CharField(choices=[('Create', 'Создана'), ('Started', 'Отправлено'), ('Done', 'Завершена')], default='Create', max_length=50, verbose_name='Статус рассылки')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.mailingmessage', verbose_name='Сообщение')),
                ('recipients', models.ManyToManyField(to='recipient.recipient', verbose_name='Получатели')),
            ],
            options={
                'verbose_name': 'Настройка рассылки',
                'verbose_name_plural': 'Настройка рассылок',
            },
        ),
        migrations.CreateModel(
            name='MailingStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_datetime', models.DateTimeField(auto_now_add=True, verbose_name='last_datetime (последняя дата отправки)')),
                ('status', models.BooleanField(default=False, verbose_name='статус отправки')),
                ('mailing_response', models.TextField(verbose_name='почтовый запрос (ответ сервера)')),
                ('mailing_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.mailingsettings', verbose_name='рассылка')),
                ('recipient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recipient.recipient', verbose_name='клиент рассылки')),
            ],
            options={
                'verbose_name': 'Статус отправки',
                'verbose_name_plural': 'Статусы отправки',
            },
        ),
    ]
