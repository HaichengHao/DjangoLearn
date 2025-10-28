#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Djangolearn 
@File    ：urls.py
@IDE     ：PyCharm 
@Author  ：百年
@Date    ：2025/10/20 15:28 
'''

from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('login/',views.login,name='login'),
    #tips:上面都是FBV,也就是一个路由对应一个函数,
    #important:下面的路由我们写一个CBV,也就是一个路由对应一个类
    path('auth/',views.UserView.as_view(),name='auth') #tips:这里第二个参数指定我们的类名,并在后头加上.as_view,这是规定
]