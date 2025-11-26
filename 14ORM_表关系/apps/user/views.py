from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from django.views import View
from .models import Depart,User,Role

def index(request):
    User.objects.create(name='zhangsan',dp=1)
    return HttpResponse('ok')
