import os

BROKER_URL = 'redis://localhost:6379/1'

from celery import Celery

app = Celery('updater', backend = BROKER_URL, broker = BROKER_URL)

@app.task
def update_task():
    os.system('git pull origin master')
    os.system('celery multi restart node1 -A distributed --loglevel=info --pidfile=distributed.pid')

def update():
    update_task.delay().get()
