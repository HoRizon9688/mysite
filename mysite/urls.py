"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app01 import views
from mysite import testdb
urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert/', testdb.insert),
    path('update/', testdb.update),
    path('delete/', testdb.delete),
    path('login/', views.login),
    path('set_cookie/', views.set_cookie),
    path('get_cookie/', views.get_cookie),
    path('index/', views.open_index),
]
