worker:
	celery multi start 1 -A distributed --loglevel=info --pidfile=worker.pid

redis:
	docker run -p 0.0.0.0:6379:6379 -ti redis