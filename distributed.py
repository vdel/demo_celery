import json

BROKER_URL = 'redis://:1234@localhost:6379/0'

from celery import Celery

app = Celery('distributed', backend = BROKER_URL, broker = BROKER_URL)

@app.task
def compute_task(config_file_name, config_file_data, x):
    with open(config_file_name, 'w') as f:
        f.write(config_file_data)

    # Do the job as is you were on local computer
    with open(config_file_name, 'r') as f:
        data = json.load(f)

    return data['z']

def compute(config_file, x):
    with open(config_file, 'r') as f:
        config_file_data = f.read()
    t = compute_task.delay(config_file, config_file_data, x)

    # Do some more job here
    y = 1
    while y < 100:
        y = y * 2

    return t.get() + y + x

