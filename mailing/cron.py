import smtplib

from dateutil.relativedelta import relativedelta
from django.core.mail import send_mail
from datetime import datetime, timedelta
import pytz
from config import settings
from mailing.models import MailingSettings, MailingStatus, LOGS_STATUS_CHOICES


def send_mailing():
    zone = pytz.timezone(settings.TIME_ZONE)
    current_time = datetime.now(zone)

    mailing_settings = MailingSettings.objects.filter(first_datetime__lte=current_time).filter(
        sending_status__in=['Create', 'Started'])
    for mailing in mailing_settings:
        if mailing.first_datetime is None:
            mailing.first_datetime = current_time
        title = mailing.message.title
        content = mailing.message.content
        mailing.sending_status = 'Started'
        mailing.save()
        try:
            if mailing.end_time < mailing.first_datetime:
                mailing.first_datetime = current_time
                mailing.sending_status = 'Done'
                mailing.save()
                continue
            if mailing.first_datetime <= current_time:
                server_response = send_mail(
                    subject=title,
                    message=content,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[recipient.email for recipient in mailing.recipients.all()],
                    fail_silently=False,
                )
                if server_response == 1:
                    server_response = 'Сообщение отправлено'
                MailingStatus.objects.create(sending_status=True, mailing_response=server_response, mailing_list=mailing)

                if mailing.sending_period == 'daily':
                    mailing.next_datetime = current_time + timedelta(days=1)

                elif mailing.sending_period == 'weekly':
                    mailing.next_datetime = current_time + timedelta(days=7)

                elif mailing.sending_period == 'monthly':
                    mailing.next_datetime = current_time + relativedelta(months=1)

            mailing.save()

        except smtplib.SMTPException as error:
            MailingStatus.objects.create(mailing_response=error, mailing_list=mailing)
