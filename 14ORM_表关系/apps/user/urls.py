#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Djangolearn 
@File    ：urls.py
@IDE     ：PyCharm 
@Author  ：百年
@Date    ：2025/11/24 16:16 
'''


from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('index/',views.index,name='index')
]