import distributed

r = distributed.update.delay()
print r.get()

r = distributed.version.delay()
print r.get()