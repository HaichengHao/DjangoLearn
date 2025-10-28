#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Djangolearn 
@File    ：urls.py
@IDE     ：PyCharm 
@Author  ：百年
@Date    ：2025/10/13 20:15 
'''
from django.http import HttpResponse
from django.urls  import path



def login(request):
    return HttpResponse('你好,欢迎登陆')


urlpatterns = [
    path('login/', login)
]