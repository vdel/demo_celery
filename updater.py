import os
import redis_config
from celery import Celery

BROKER_URL = redis_config.get_broker_url(1)
app = Celery('updater', backend = BROKER_URL, broker = redis_config.BROKER_URL)

@app.task
def update_task():
    os.system('git pull origin master')
    os.system('celery multi restart node1 -A distributed --loglevel=info --pidfile=distributed.pid')

def update():
    update_task.delay().get()
