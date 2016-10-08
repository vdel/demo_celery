import os

BROKER_URL = os.getenv('BROKER_URL', 'redis://localhost:6379/0')

from celery import Celery

app = Celery('distributed', backend = BROKER_URL, broker = BROKER_URL)

@app.task
def update():
    os.system('git pull origin master')
    os.spawnl(os.P_NOWAIT, 'celery multi restart 1 -A distributed --loglevel=info --pidfile=worker.pid')

@app.task
def version():
    return 2

