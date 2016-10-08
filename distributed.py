import os

BROKER_URL = 'redis://localhost:6379/0'

from celery import Celery

app = Celery('distributed', backend = BROKER_URL, broker = BROKER_URL)

@app.task
def update():
    os.system('git pull origin master')

@app.task
def version():
    return 2

@app.task
def add(x, y):
    return x + y