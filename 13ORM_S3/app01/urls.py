#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Djangolearn 
@File    ：urls.py
@IDE     ：PyCharm 
@Author  ：百年
@Date    ：2025/11/12 15:29 
'''
from django.urls import path
from . import views

app_name = 'app01'
urlpatterns = [
    path('index/', views.index, name='index')
]

