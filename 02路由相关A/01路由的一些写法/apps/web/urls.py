#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Djangolearn 
@File    ：urls.py
@IDE     ：PyCharm 
@Author  ：百年
@Date    ：2025/10/13 20:20 
'''
from django.urls import path
from .views import home,article
urlpatterns = [
    path('home/',home),
    path('article/',article)
]