#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Djangolearn 
@File    ：urls.py
@IDE     ：PyCharm 
@Author  ：百年
@Date    ：2025/11/4 14:17 
'''
from django.urls  import path,include
from . import views
app_name = 'user'
urlpatterns = [
    path('index/',views.index,name='index'),

]