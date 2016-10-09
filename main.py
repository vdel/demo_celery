import updater
import distributed

updater.update()

print(distributed.compute('config.json', 1))
