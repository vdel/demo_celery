REDIS_HOST='127.0.0.1'
REDIS_PASSWORD = '1234'
BROKER_URL = 'redis://:%s@%s:6379/%%d' % (REDIS_PASSWORD, REDIS_HOST)

def get_broker_url(db_id):
    return BROKER_URL % db_id