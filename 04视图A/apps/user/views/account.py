#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Djangolearn 
@File    ：account.py
@IDE     ：PyCharm 
@Author  ：百年
@Date    ：2025/10/17 17:07 
'''

from django.shortcuts import render,HttpResponse

def login(request):
    return HttpResponse('登录界面')

def auth(request):
    return HttpResponse('授权管理界面')