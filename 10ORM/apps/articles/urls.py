#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Djangolearn 
@File    ：urls.py
@IDE     ：PyCharm 
@Author  ：百年
@Date    ：2025/11/4 14:20 
'''
from django.urls  import path
from . import views
app_name = 'articles'
urlpatterns = [
    path('articlelist/',views.article_list,name='articlelist')
]