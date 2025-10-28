#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Djangolearn 
@File    ：urls.py
@IDE     ：PyCharm 
@Author  ：百年
@Date    ：2025/10/15 12:29 
'''

from django.urls import path
from . import views

app_name = 'web'
urlpatterns = [
    path('home/',views.home,name='home' ),
    path('login/',views.login,name='login')
]