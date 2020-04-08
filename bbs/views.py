import requests
from lxml import etree
from django.shortcuts import render, HttpResponse, redirect,get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.contenttypes.models import ContentType
from django.db.models import Count
from bbs.models import *
from comment.models import Comment
from bbs.forms import LoginForm, RegForm, PublishForm
from comment.forms import CommentForm
from rest_framework import generics
from bbs.serializers import *
from django.contrib.auth.decorators import login_required
# Create your views here.


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


def index(request):
    category_list = Category.objects.all()
    post_list = Post.objects.all()
    if request.is_ajax():
        return render(request, 'bbs/post_list.html',locals())
    return render(request, 'bbs/index.html', locals())


def acc_login(request):
    # if request.method == "POST":
    #     referer = request.POST.get('referer')
    #     print(referer)
    #     user = authenticate(username=request.POST.get('username'),
    #                         password=request.POST.get('password'))
    #     if user:
    #         login(request, user)
    #         print(referer)
    #         return redirect(referer)
    #     else:
    #         login_error = '用户名密码错误'
    #         return render(request, 'bbs/login.html',{'login_error': login_error})
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            login(request, user)
            return redirect(request.GET.get('from'), '/')
    else:
        login_form = LoginForm()
    return render(request, 'bbs/login.html', locals())


def acc_logout(request):
    logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            password = reg_form.cleaned_data['password']
            # 创建用户
            user = User.objects.create_user(username=username, password=password)
            user_profile = UserProfile(user=user, name=username)
            user_profile.save()
            # 登录用户
            user_login = authenticate(username=username, password=password)
            login(request, user_login)
            return redirect(request.GET.get('from'), '/')
    else:
        reg_form = RegForm()
    return render(request, 'bbs/register.html',locals())


# 版块页
def category(request):
    category_list = Category.objects.all()
    return render(request, 'bbs/category.html', locals())


# 版块详情页
def caregorydetail(request):
    category_name = request.GET.get('name')
    theme_pk = request.GET.get('theme')
    comment = request.GET.get('comment')
    category_detail = Category.objects.get(name=category_name)
    theme_list = Theme.objects.filter(category=category_detail)
    post_list = Post.objects.filter(category_id=category_detail.pk)
    comment_order = 1
    comment_label = 'dropup'
    if theme_pk:
        post_list = Post.objects.filter(category_id=category_detail.pk, theme_id=theme_pk)
    elif comment == '1':
        post_list = Post.objects.filter(category_id=category_detail.pk).order_by('-comment_count')
        comment_order = 0
        comment_label = 'dropdown'
    elif comment == '0':
        post_list = Post.objects.filter(category_id=category_detail.pk).order_by('comment_count')
        comment_order = 1
        comment_label = 'dropup'
    else:
        post_list = Post.objects.filter(category_id=category_detail.pk)
    if request.is_ajax():
        if theme_pk:
            post_list = Post.objects.filter(category_id=category_detail.pk, theme_id=theme_pk)
        elif comment == '1':
            post_list = Post.objects.filter(category_id=category_detail.pk).order_by('-comment_count')
        elif comment == '0':
            post_list = Post.objects.filter(category_id=category_detail.pk).order_by('comment_count')
        else:
            post_list = Post.objects.filter(category_id=category_detail.pk)
        return render(request, 'bbs/post_list.html',locals())
    return render(request, 'bbs/caregorydetail.html', locals())


# 帖子详情页
def postdetail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post_content_type = ContentType.objects.get_for_model(post)
    comments = Comment.objects.filter(content_type=post_content_type, object_id=post_id, parent=None).order_by('comment_time')
    data = {'content_type': post_content_type.model,'object_id': post_id,'reply_comment_id': 0}
    comment_form = CommentForm(initial=data)
    reply_form = CommentForm(initial=data)
    return render(request, 'bbs/postdetail.html', locals())


# 发表帖子
def publish(request):
    category_list = Category.objects.all()
    pubform = PublishForm()
    if request.method == 'POST':
        pubform = PublishForm(request.POST)
        if pubform.is_valid():
            content = pubform.cleaned_data['content']
        post_category = request.POST.get('post-category')
        post_theme = request.POST.get('post-theme')
        title = request.POST.get('post-title')
        post_content = request.POST.get('editor1')
        user_id = request.user.id
        post = Post()
        post.category = Category.objects.get(id=post_category)
        post.theme = Theme.objects.get(name=post_theme, category=post_category)
        post.title = title
        post.content = content
        post.author = UserProfile.objects.get(id=user_id)
        post.save()
        return redirect('/')

    return render(request, 'bbs/publish_post.html', locals())


# 版块 主题联动选择
def linked(request):
    category_id = request.GET.get('category_id')
    theme_list = Theme.objects.filter(category_id=category_id).values('name')
    # print(theme_list)
    data = {'theme_list': list(theme_list)}
    return JsonResponse(data)


def addpost(request):
    for i in range(6):
        base_url = 'http://jianyuluntan.com/?order=&page={}'.format(i)
        response = requests.get(base_url)
        html_str = etree.HTML(response.text)
        div_list = html_str.xpath('//div[@class="col-md-9"]/div[position()>1]')
        for div in div_list:
            title = div.xpath('./div/h6/a/text()|./div/h5/a[3]/text()')[0]
            url = 'http://jianyuluntan.com'+div.xpath('./div/h6/a/@href|./div/h5/a[3]/@href')[0]
            detail = requests.get(url)
            detail_str = etree.HTML(detail.text)
            content = detail_str.xpath('string(//div[@class="zhengwen"])').strip()
            user = UserProfile.objects.first()
            category = Category.objects.first()
            post = Post()
            post.title = title
            post.content = content
            post.author = user
            post.category = category
            post.save()
    return HttpResponse('1')