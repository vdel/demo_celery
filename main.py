import updater
import distributed

updater.update()

r = distributed.version.delay()
print(r.get())