"""day01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from apps.web import views
from django.contrib import admin
from django.urls import path,re_path,include
#tips:主路由
# urlpatterns = [
#     path('admin/', admin.site.urls),#tips:组成部分一般是path('路由',对应的函数)
#     #important:其实路由的函数一般写在apps中对应的app的view中,如果要用的话引入到这里即可
#     path('home/',views.home),
#     path('news/<int:nid>/',views.news), #tips:其实这是django借鉴的flask的类型验证
#     path('article/',views.article),
#     path('pathdetect/<path:pinfo>',views.pathdetect),
#     re_path(r'regxtst/(\d+)/',views.regxtst) #important:注意加上r进行转译
# ]
'''
指定路径参数的类型验证有多个类型可以选择
int,整数
str,字符串
slug, 字母+数字+下划线
uuid,uuid格式

path,路径
'''

#tips:下面的知识点是关于路由分发的,相当于注册蓝图
urlpatterns = [
    path('web/',include("apps.web.urls")),
]