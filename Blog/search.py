"""this is a search class"""
# bin/bash python
from django.http import HttpResponse
from django.shortcuts import render_to_response


# 表单
def search_form(request):
    """表单"""
    request.encoding = 'utf-8'
    return render_to_response("search_form.html")


# 接收请求的数据
def search(request):
    """接收请求的数据"""
    request.encoding = 'utf-8'
    if 'q' in request.GET:
        message = '你搜到的内容为:'+ request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)