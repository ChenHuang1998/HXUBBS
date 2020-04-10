from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import authenticate
from comment.models import Comment
from comment.forms import CommentForm
from bbs.models import *
# Create your views here.


def update_comment(request):
    # if not request.user.is_authenticated:
    #     return HttpResponse('未登录')
    # text = request.POST.get('text', '').strip()
    # if text == '':
    #     return HttpResponse('不能为空')
    # try:
    #     content_type = request.POST.get('content_type', '')
    #     object_id = int(request.POST.get('object_id', ''))
    #     model_class = ContentType.objects.get(model=content_type).model_class()
    #     model_obj = model_class.objects.get(id=object_id)
    # except Exception as e:
    #     return HttpResponse('出错')
    # comment = Comment()
    # comment.user = request.user.userprofile
    # comment.text = text
    # comment.content_object = model_obj
    # comment.save()
    # referer = request.META.get('HTTP_REFERER', '/')
    # return redirect(referer)

    referer = request.META.get('HTTP_REFERER', '/')
    data = {}
    comment_form = CommentForm(request.POST, user=request.user)
    if comment_form.is_valid():
        comment = Comment()
        comment.user = request.user.userprofile
        comment.text = comment_form.cleaned_data['text']
        comment.content_object = comment_form.cleaned_data['content_object']
        parent = comment_form.cleaned_data['parent']
        if parent is not None:
            comment.root = parent.root if parent.root is not None else parent
            comment.parent = parent
            comment.reply_to = parent.user
        comment.save()
        data['status'] = 'SUCCESS'
        data['user_name'] = comment.user.name
        data['user_head'] = str(comment.user.image)
        data['comment_time'] = comment.comment_time.strftime('%Y-%m-%d %H:%M')
        data['text'] = comment.text
        data['content_type'] = ContentType.objects.get_for_model(comment).model
        if parent is not None:
            data['reply_to'] = comment.reply_to.name
        else:
            data['reply_to'] = ''
        data['pk'] = comment.id
        data['root_pk'] = comment.root.id if comment.root is not None else ''
    else:
        data['status'] = 'ERROR'
        data['message'] = list(comment_form.errors.values())[0][0]
    return JsonResponse(data)