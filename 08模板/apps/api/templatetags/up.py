#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Djangolearn 
@File    ：up.py
@IDE     ：PyCharm 
@Author  ：百年
@Date    ：2025/10/24 16:10 
'''

from django import template

register = template.Library()

@register.filter
def upw(value):
    return value.upper()

@register.filter
def rev(value:list):
    return value.reverse()

@register.simple_tag
def mytag():
    return 'aloha'


@register.simple_tag
def mytag2(a1:str,a2:str):
    return a1+'hihih'+a2


@register.inclusion_tag('api/demo.html')
def mytag3():
    return {'name':'张三','age':20}