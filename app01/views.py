from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# 登录
def login(request):
    if request.method == "POST":
        if request.POST.get('user_name') == 'HoRizon' and request.POST.get('user_password') == '123456789':
            request.session['username'] = request.POST.get('user_name')
            request.session['is_login'] = True
            return HttpResponseRedirect('/index/')
        else:
            return HttpResponse("账号或密码错误,请返回")
    else:
        return render(request, "login.html", locals())


def logout(request):
    if request.method == "GET":
        request.session.flush()
        return HttpResponseRedirect('/login/')


# 设置cookie
def set_cookie(request):
    rsp = HttpResponse()
    rsp.set_cookie('username', 'fanxiaowei', 3600)
    return rsp


# 查看cookie
def get_cookie(request):
    value = request.COOKIES.get('username')
    return render(request, 'cookie.html', {"cookie": value})


def open_index(request):
    if request.session.get('is_login', False):
        return render(request, "index.html")
    else:
        return render(request, 'back2login.html')
