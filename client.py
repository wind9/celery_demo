from celery_app import task1
from celery_app import task2


task1.add.apply_async(args=[2, 8], queue='email', routing_key='email')
task2.multiply.apply_async(args=[3, 7], queue='pageview', routing_key='pageview')

print('hello world')