worker:
	celery -A distributed worker --loglevel=info
	#--autoreload --include=distributed

redis:
	docker run -p 0.0.0.0:6379:6379 -ti redis