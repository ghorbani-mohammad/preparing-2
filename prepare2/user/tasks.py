import time
from celery import shared_task

@shared_task()
def send_email(to, subject, body):
    # suppose that each sending email takes about 1 second
    time.sleep(1)
