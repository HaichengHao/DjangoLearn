#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Djangolearn 
@File    ：urls.py
@IDE     ：PyCharm 
@Author  ：百年
@Date    ：2025/12/2 17:22 
'''

from django.urls import path
from .views import index
app_name = 'user'

urlpatterns = [
    path('index/',index,name='index')
]