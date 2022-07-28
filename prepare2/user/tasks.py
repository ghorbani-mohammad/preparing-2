from celery import shared_task

@shared_task()
def send_email(to, subject, body):
    pass
