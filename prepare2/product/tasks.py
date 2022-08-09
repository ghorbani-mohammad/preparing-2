import time
from random import choice
from celery import shared_task, Task

from . import models


class BaseTaskWithRetry(Task):
    autoretry_for = (Exception,)
    retry_kwargs = {"max_retries": 10}
    retry_backoff = 5
    retry_jitter = True


@shared_task
def process_product_image(product_id):
    # suppose that each product image processing takes about 1 second
    time.sleep(2)


@shared_task
def periodic_task():
    print('running the periodic task')


@shared_task
def example_async_task(product_id):
    product = models.Product.objects.get(pk=product_id)
    time.sleep(20)


@shared_task(base=BaseTaskWithRetry)
def retry_task(product_id):
    failed = choice([True, False])
    if failed:
        raise Exception()
