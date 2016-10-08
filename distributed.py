import os

BROKER_URL = 'redis://localhost:6379/0'

from celery import Celery

app = Celery('distributed', backend = BROKER_URL, broker = BROKER_URL)

@app.task
def update():
    os.system('git pull origin master')
    os.system('celery multi restart 1 --pidfile=worker.pid')

@app.task
def version():
    return 2

