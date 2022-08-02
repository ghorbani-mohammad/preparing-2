import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "prepare2.settings")
app = Celery("prepare2")
app.config_from_object("django.conf.settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "periodic_task": {
        "task": "product.tasks.periodic_task",
        "schedule": crontab(minute='*'),
    }
}
