from django.shortcuts import render,HttpResponse

from app01 import models as m1
from app02 import models as m2
# Create your views here.
# from app02.models import Role
def index(request):

    #tips:操作app01中的models中的表
    #创建一条数据
    m1.Userinfo.objects.create(name='judy')
    #读取
    res =m1.Userinfo.objects.all()
    print(res)

    #tips:操作app02中的models中的表
    #创建一条数据
    m2.Role.objects.create(role_name='niko')
    res = m2.Role.objects.all()
    print(res)

    return HttpResponse('ok')
