import time
from celery import shared_task

@shared_task
def process_product_image(product_id):
    time.sleep(2)