"""处理post请求"""
#bin/bash python

from django.shortcuts import render
from django.views.decorators import csrf
from django.shortcuts import render_to_response

def post(request):
    """post提交表单"""
    request.encoding = 'utf-8'
    return render_to_response('post.html')

#接收post请求数据
def search_post(request):
    """处理post请求"""
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']
        return render(request, 'post.html', ctx)
