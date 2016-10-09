REDIS_PASSWORD = '1234'
BROKER_URL = 'redis://:%s@localhost:6379/%d'

def get_broker_url(db_id):
    return BROKER_URL % (REDIS_PASSWORD, db_id)