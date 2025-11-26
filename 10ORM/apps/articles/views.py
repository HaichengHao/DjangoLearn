from django.shortcuts import render,HttpResponse

# Create your views here.

def article_list(request):
    return HttpResponse('这是书籍页面')