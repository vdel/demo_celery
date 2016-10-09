worker:
	celery multi start node1 -A distributed --loglevel=info --pidfile=distributed.pid
	celery multi start node2 -A updater --loglevel=info --pidfile=updater.pid

stop:
	celery multi stop node1 --pidfile=distributed.pid
	celery multi stop node2 --pidfile=updater.pid

redis:
	docker run -d -p 0.0.0.0:6379:6379 --name redis redis redis-server --requirepass 1234