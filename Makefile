worker:
	celery multi start 1 -A distributed --loglevel=info --pidfile=distributed.pid
	celery multi start 2 -A updater --loglevel=info --pidfile=updater.pid

stop:
	celery multi stop 1 --pidfile=distributed.pid
	celery multi stop 2 --pidfile=updater.pid

redis:
	docker run -p 0.0.0.0:6379:6379 -ti redis