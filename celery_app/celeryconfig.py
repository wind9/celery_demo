from kombu import Queue
from kombu import Exchange


redis_host = '121.15.10.34'
redis_port = 8912
redis_password = 'test@2019'
broker_url = 'redis://:{}@{}:{}/0'.format(redis_password, redis_host, redis_port)
celery_result_backend = 'redis://:{}@{}:{}/1'.format(redis_password, redis_host, redis_port)
celery_timezone = 'Asia/Shanghai'
celery_imports = (
    'celery_app.task1',
    'celery_app.task2'
)
task_queues = (
    Queue('default', exchange=Exchange('default'), routing_key='default'),
    Queue('email', exchange='email', routing_key='email'),
    Queue('pageview', exchange='pageview', routing_key='pageview')
)
task_routes = {
    'celery_app.task1.add': {'queue':'email', 'routing_key':'email'},
    'celery_app.task2.multiply': {'queue':'pageview', 'routing_key':'pageview'}
}
