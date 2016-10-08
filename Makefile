worker:
	env CELERYD_FSNOTIFY=stat celery worker -A distributed --loglevel=info --autoreload

redis:
	docker run -p 0.0.0.0:6379:6379 -ti redis