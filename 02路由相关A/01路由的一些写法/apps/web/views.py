from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return HttpResponse("主页")


def news(request, nid):
    print(nid) #打印接受到的nid
    return HttpResponse(nid)


def article(request):
    aid = request.GET.get('aid') #tips：结合flask来理解,这其实很像request.args.get()
    return HttpResponse(f'{aid}')

def pathdetect(request,pinfo):
    print(pinfo)
    return HttpResponse(pinfo)

def regxtst(request,xid):
    print(xid) #tips:打印接收到的xid
    return HttpResponse('成功')