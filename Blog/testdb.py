from django.http import HttpResponse
from TestModel.models import Test


def testdb(request):
    if request:
        test1 = Test(name='zhangshuyu')
        test1.save()
        return HttpResponse('<p>数据添加成功</p>')
