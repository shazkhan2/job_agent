from celery import shared_task
import time
import logging

logger = logging.getLogger(__name__)

@shared_task
def add_numbers(x, y):
    logger.info(f"Adding {x} and {y}...")
    time.sleep(5) 
    result = x + y
    logger.info(f"Addition complete: {result}")
    return result

@shared_task
def debug_celery_status():
    logger.info("Celery debug task running successfully!")
    return "Celery is alive!"