from django.http import HttpResponse
from django.shortcuts import render
from django import forms


class LoginForm(forms.Form):
    user_name = forms.CharField(label="用户名", min_length=6, max_length=12)
    user_password = forms.CharField(label="用户密码", min_length=8)


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponse("登录成功")
    else:
        form = LoginForm()
    return render(request, "login.html", locals())


def set_cookie(request):
    rsp = HttpResponse()
    rsp.set_cookie('username', 'fanxiaowei', 3600)
    return rsp


def get_cookie(request):
    value = request.COOKIES.get('username')
    return render(request, 'cookie.html', {"cookie": value})
