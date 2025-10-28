#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Djangolearn 
@File    ：urls.py
@IDE     ：PyCharm 
@Author  ：百年
@Date    ：2025/10/28 16:18 
'''
from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('usercenter/',views.UserCenterView.as_view(),name='usercenter')
]