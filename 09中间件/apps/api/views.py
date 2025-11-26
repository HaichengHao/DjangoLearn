from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
# Create your views here.

#tips:如何使用templateresponse
from django.template.response import TemplateResponse

def index(request):
    print('函数被执行了')
    # return HttpResponse("hello")
    # return render(request,'api/index.html')
    return TemplateResponse(request,'api/index.html')
class UserCenterView(View):
    def get(self, request):
        return HttpResponse('被访问了')
    def post(self, request):
        name = request.POST.get('name')
        print(name)
        return HttpResponse('提交了东西')