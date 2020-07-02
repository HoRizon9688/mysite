from django.http import HttpResponse
from app01.models import Test


# 数据库操作
def insert(request):
    test1 = Test(name='abc')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")


def update(request):
    Test.objects.all().update(name='Google')
    return HttpResponse("<p>数据更新成功</p>")


def delete(request):
    Test.objects.all().delete()
    return HttpResponse("<p>数据删除成功</p>")