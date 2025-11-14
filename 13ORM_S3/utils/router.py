#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Djangolearn 
@File    ：router.py
@IDE     ：PyCharm 
@Author  ：百年
@Date    ：2025/11/12 16:48 
'''
from django.db.models.options import Options


class Router(object):
    # def db_for_read(self, model, **hints):
    #     print('--------------------------------------------')
    #     print(model._meta.app_label) #tips:操作的是哪个app
    #     print(model._meta,type(model._meta)) #app01.userinfo <class 'django.db.models.options.Options'>
    #     print(model._meta.model_name) #tips:表名称
    #     print(hints)
    #     return 'back'
    #     # return 'default'
    #
    # def db_for_write(self,model,**hints):
    #     return 'default'

    # 分库操作
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'app01':
            return 'default'
        elif model._meta.app_label == 'app02':
            return 'back'
    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'app01':
            return 'default'
        elif model._meta.app_label == 'app02':
            return 'back'
    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        控制 migrate 命令是否在某个数据库上执行
        """
        if app_label == 'app01':
            return db == 'default'
        elif app_label == 'app02':
            return db == 'back'
        return None
