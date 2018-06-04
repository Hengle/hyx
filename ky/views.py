from django.shortcuts import render
from django.http.response import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def index(request):
    print(request.user)
    return render(request, 'pages/index.html')

@login_required
def dev(request):
    return render(request,'pages/dev.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'account/login.html')
    else:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(('/'))
        else:
            return render(request, 'status/500.html', dict(error='密码错误'))

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')

