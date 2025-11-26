from django.shortcuts import render, HttpResponse, redirect, reverse


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        return redirect(reverse('user:auth'))
    return render(request, 'user/login.html')


def auth(request):
    res = HttpResponse('你好!!!')
    res.headers['login'] = 'login_'
    res.set_cookie('username', 'xxx',max_age=60480)
    return res


