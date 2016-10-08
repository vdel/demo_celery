import distributed

r = distributed.update.delay()
print r.get()