#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Djangolearn 
@File    ：md.py
@IDE     ：PyCharm 
@Author  ：百年
@Date    ：2025/10/28 16:09 
'''

class MyMD(object):

    def __init__(self,get_response):
        self.get_response = get_response


    def __call__(self, request):
        # tips:请求进来的时候走的是这里
        print('请求来了')
        response = self.get_response(request)  # tips:这一步其实就是执行视图函数
        # tips:请求从这里再出去
        print('请求处理完成了')
        return response