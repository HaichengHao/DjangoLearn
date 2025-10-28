#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Djangolearn 
@File    ：urls.py
@IDE     ：PyCharm 
@Author  ：百年
@Date    ：2025/10/20 13:03 
'''
from .views import auth,login
from django.urls import path

app_name = 'user'
urlpatterns = [
    path('login/',login,name='login'),
    path('auth/',auth,name='auth')
]