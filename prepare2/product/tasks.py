import time
from celery import shared_task

@shared_task
def process_product_image(product_id):
    # suppose that each product image processing takes about 1 second
    time.sleep(2)