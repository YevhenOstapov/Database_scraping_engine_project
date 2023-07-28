import os

from celery import Celery


broker = os.environ.get('BROKER_URL')
app = Celery(
    'celery_module',
    broker=broker,
    include=['celery_module.tasks'],
    backend='db+sqlite:///results.db',
)
