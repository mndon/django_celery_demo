# -*- coding: utf-8 -*-
# @Time    : 2022/4/28 9:50
# @Author  : LinMD
# @File    : tasks.py.py
# @Desc    :
from celery import shared_task
from .models import Entity


@shared_task
def get_entity():
    w = Entity.objects.all()
    print(w[0].imp)
    print(w)

