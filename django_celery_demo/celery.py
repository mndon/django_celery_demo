# -*- coding: utf-8 -*-
# @Time    : 2022/4/28 9:46
# @Author  : LinMD
# @File    : celery.py
# @Desc    :
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_demo.settings')

app = Celery("django_celery_demo")

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
