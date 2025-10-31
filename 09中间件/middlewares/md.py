#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Djangolearn 
@File    ：md.py
@IDE     ：PyCharm 
@Author  ：百年
@Date    ：2025/10/28 16:09 
'''
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse


# class MyMD(object):
#
#     def __init__(self,get_response):
#         self.get_response = get_response
#
#
#     def __call__(self, request):
#         # tips:请求进来的时候走的是这里
#         # print('请求来了')
#         # response = self.get_response(request)  # tips:这一步其实就是执行视图函数
#         # # tips:请求从这里再出去
#         # print('请求处理完成了')
#         # return response
#
#         #另外一种写法
#         if hasattr(self, 'process_request'):
#            self.process_request(request)
#         response = self.get_response(request)
#         if hasattr(self, 'process_response'):
#             self.process_response(request, response)
#         return response
#     def  process_request(self, request):
#         print('请求来了')
#     def process_response(self, request, response):
#         print('请求处理完成了')

# important:最优解,继承MiddlewareMixin
class MyMD(MiddlewareMixin):
    def process_request(self, request):
        print('请求来了1')

    def process_response(self, request, response):
        print('请求走了1')
        return response  # important:注意一定要加上返回值,这一点也有些像scrapy中间件中的传递一样,必须有返回值


class MyMD2(MiddlewareMixin):
    def process_request(self, request):
        print('请求来了2')
        # return HttpResponse('myMD2对请求进行了处理并触发')

    def process_view(self, request, view_func, view_args,
                     view_kwargs):  # view_func 路由匹配成功之后的视图函数,也就是说如果匹配成功那就执行指定的这个view_func视图函数
        print(request, view_func)
        return HttpResponse('返回')

    def process_response(self, request, response):
        print('请求走了2')
        return response


class MyMD3(MiddlewareMixin):
    def process_request(self, request):
        print('请求来了3')

    def process_response(self, request, response):
        print('请求走了3')
        return response
