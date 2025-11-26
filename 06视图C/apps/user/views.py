from django.shortcuts import render,HttpResponse
from django.views import View
# Create your views here.

def login(request):
    if request.method == 'GET':
        return HttpResponse('登陆界面')


# #important:如果想要使用CBV,就必须继承django.views 中的View
class UserView(View):

    def get(self,request):
        #如果请求方式是get方式就执行下面的函数
        return HttpResponse('授权界面')
    def post(self,request):
        #如果请求方式是post方式就执行下面的函数
        pass