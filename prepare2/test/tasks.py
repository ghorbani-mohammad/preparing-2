from celery import shared_task

@shared_task()
def check_job_pages():
    print('ok')