import time
from . import models
from celery import shared_task


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
