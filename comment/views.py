from django.shortcuts import render, redirect, HttpResponse
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import authenticate
from comment.models import Comment
from bbs.models import *
# Create your views here.


def update_comment(request):
    if not request.user.is_authenticated:
        return HttpResponse('未登录')
    text = request.POST.get('text', '').strip()
    if text == '':
        return HttpResponse('不能为空')
    try:
        content_type = request.POST.get('content_type', '')
        object_id = int(request.POST.get('object_id', ''))
        model_class = ContentType.objects.get(model=content_type).model_class()
        model_obj = model_class.objects.get(id=object_id)
    except Exception as e:
        return HttpResponse('出错')
    comment = Comment()
    comment.user = request.user.userprofile
    comment.text = text
    comment.content_object = model_obj
    comment.save()
    referer = request.META.get('HTTP_REFERER', '/')
    return redirect(referer)