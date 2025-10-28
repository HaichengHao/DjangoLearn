#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Djangolearn 
@File    ：urls.py
@IDE     ：PyCharm 
@Author  ：百年
@Date    ：2025/10/17 17:09 
'''
from .views import account,order
from django.urls import path

app_name = 'user'
urlpatterns = [
    path('login/',account.login,name='login'),
    path('auth/',account.auth,name='auth')
]
