from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse, request
from django.urls import reverse


def home(request):
    return HttpResponse("主页")


def login(request):
    #tips:先判断是什么请求
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        return redirect(reverse('home'))
    return render(request, 'login.html')


def auth(request):
    return HttpResponse('先进行授权')


def add(request):
    url = reverse('auth')
    return redirect(url)
    # return HttpResponse("用户添加操作")


def delete(request):
    return HttpResponse('用户删除操作')
