#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Djangolearn 
@File    ：urls.py
@IDE     ：PyCharm 
@Author  ：百年
@Date    ：2025/10/21 19:43 
'''

from django.urls import path
from . import views
app_name = 'user'
urlpatterns = [
    path('index/',views.UserView.as_view(),name='index')
]