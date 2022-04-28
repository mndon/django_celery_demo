# 使用教程

1. 根据https://docs.celeryq.dev/en/latest/django/first-steps-with-django.html，
在工程目录下新建或者修改django_celery_demo/django_celery_demo/celery.py, django_celery_demo/django_celery_demo/__init__.py， app目录下新建tasks.py


2. windows来通过单线程形式开发celery
启动命令： celery -A django_celery_demo  worker -P solo -l INFO


3. 在app views.py内调用任务的.delay调用celery一步任务