import time
from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_email(email):
    subject = 'Helo from Celery'
    message = 'This is a test email sent asynchronously with Celery.'

    time.sleep(5)
    return send_mail(
        subject, message, 'mohammad.ghorbani@hotmail.com', [email], fail_silently=False
    )
