import distributed

r = distributed.update.delay()

r = distributed.version.delay()
print(r.get())