import logging
from datetime import datetime
from time import sleep

from celery.schedules import crontab

from celery_module.celery_app import app
from config import CURRENT_TIME_ZONE
from logging_module.logger import Logger
from manager import Manager

logger = Logger("celery_tasks")

manager = Manager()


@app.task(name="update_base")
def update_base():
    logger.info(f"{datetime.now(CURRENT_TIME_ZONE).strftime('%Y-%m-%d %H:%M:%S')}: UPDATE STARTED ...")
    for attempt in range(3):
        try:
            manager.launch()
        except Exception as error:
            logging.warning(error)
            sleep(5)
            continue
        else:
            break


app.conf.beat_schedule = {
    'DB_updating': {
        'task': 'update_base',
        'schedule': crontab(minute=1, hour=0)
    },
}
app.conf.timezone = CURRENT_TIME_ZONE
