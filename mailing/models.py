from django.db import models
from users.models import User

from recipient.models import Recipient

NULLABLE = {'null': True, 'blank': True}
FREQUENCY_CHOICES = [('daily', 'раз в день'), ('weekly', 'раз в неделю'), ('monthly', 'раз в месяц'), ]
STATUS_OF_NEWSLETTER = [("Create", 'Создана'), ("Started", 'Отправлено'), ("Done", 'Завершена'), ]
LOGS_STATUS_CHOICES = [('success', 'успешно'), ('fail', 'неуспешно'), ]


class MailingMessage(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание письма")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = "Сообщения"

    def __str__(self):
        return self.title


class MailingSettings(models.Model):
    first_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Начало рассылки")
    end_time = models.DateTimeField(verbose_name="Конец рассылки", **NULLABLE)
    sending_period = models.CharField(max_length=50, choices=FREQUENCY_CHOICES, verbose_name="Период рассылки")
    message = models.ForeignKey(MailingMessage, on_delete=models.CASCADE, verbose_name="Сообщение")
    sending_status = models.CharField(max_length=50, choices=STATUS_OF_NEWSLETTER, verbose_name="Статус рассылки", default="Create")
    recipients = models.ManyToManyField(Recipient, verbose_name="Получатели")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)

    class Meta:
        verbose_name = 'Настройка рассылки'
        verbose_name_plural = "Настройка рассылок"
        permissions = [
            ('change_mailingsettings_setting_status', 'Can change mailingsettings setting_status')
        ]

    def __str__(self):
        return f"{self.message} отправляется каждый {self.sending_period} с {self.first_datetime} для {self.recipients}"


class MailingStatus(models.Model):
    last_datetime = models.DateTimeField(auto_now_add=True, verbose_name="last_datetime (последняя дата отправки)")
    sending_status = models.BooleanField(default=False, verbose_name="статус отправки")
    mailing_response = models.TextField(verbose_name="почтовый запрос (ответ сервера)")
    mailing_list = models.ForeignKey(MailingSettings, on_delete=models.CASCADE, verbose_name='рассылка')
    recipient = models.ForeignKey(Recipient, on_delete=models.CASCADE, verbose_name='клиент рассылки', **NULLABLE)

    class Meta:
        verbose_name = 'Статус отправки'
        verbose_name_plural = "Статусы отправки"

    def __str__(self):
        return f"{self.sending_status} отправилось {self.last_datetime}, ответ сервера {self.mailing_response}"
