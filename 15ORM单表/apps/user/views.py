from django.shortcuts import render, HttpResponse
from .models import UserTb
#tips：或者from . import models,这样操作的时候直接写models.UserTb.object就可以进行操作了
# Create your views here.
def index(request):


    #tips:增操作
    newuser = UserTb.objects.create(
       name="张三",
        phone='13378978868',
        gender=1
    )

    #如何拿到自己新增的数据呢？
    print(newuser) #UserTb object (1)
    print(newuser.id) #tips:甚至可以写成newuser.pk ,代表的是primarykey,是其缩写
    print(newuser.pk)
    print(newuser.name)
    print(newuser.phone)
    print(newuser.gender)

    # users = UserTb.objects.all()  #tips:查



    return HttpResponse("这是主页")
