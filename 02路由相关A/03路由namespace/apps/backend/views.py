from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse
# Create your views here.
def home(request):
    return HttpResponse("这是主页")

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        return redirect(reverse('backend:home'))
    return render(request,'backend/login.html')