import hashlib

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django import forms

from app01.models import Test


class LoginForm(forms.Form):
    user_name = forms.CharField(label="用户名", min_length=6, max_length=12)
    user_password = forms.CharField(label="用户密码", min_length=8)


# 简易登录界面
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            test1 = Test(username=request.POST.get('user_name'), password=request.POST.get('user_password'))
            test1.save()
            return HttpResponseRedirect('/index/')
    else:
        form = LoginForm()
    return render(request, "login.html", locals())


# 设置cookie
def set_cookie(request):
    rsp = HttpResponse()
    rsp.set_cookie('username', 'fanxiaowei', 3600)
    return rsp


def get_cookie(request):
    value = request.COOKIES.get('username')
    return render(request, 'cookie.html', {"cookie": value})


def open_index(request):
    cur_name = Test.objects.values('username')
    return render(request, "index.html", {'name': cur_name})
