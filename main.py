import distributed

r = distributed.update.delay()
r.get()

r = distributed.version.delay()
print(r.get())