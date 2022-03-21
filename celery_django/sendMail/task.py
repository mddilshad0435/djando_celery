
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from celery import shared_task
from django.conf import settings

@shared_task(bind=True)
def send_mail_to_all(self):
    users = get_user_model().objects.all()
    for user in users:
        mail_subject = 'Hi! Celery Testing'
        message = "This is a code to send mail to all user"
        to_mail = user.email
        print(user.email)
        send_mail(
            subject = mail_subject,
            message = message,
            from_email = settings.EMAIL_HOST_USER,
            recipient_list = [to_mail],
            fail_silently = False,
        )
    return "Done"
