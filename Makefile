worker:
	#celery multi start 1 -A distributed --loglevel=info --pidfile=worker.pid
	celery worker -A distributed --loglevel=info --include=distributed

redis:
	docker run -p 0.0.0.0:6379:6379 -ti redis