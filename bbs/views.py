import requests
from lxml import etree
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.contenttypes.models import ContentType
from bbs.models import *
from comment.models import Comment
from bbs.forms import LoginForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    category_list = Category.objects.all()
    post_list = Post.objects.all()
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
        username = request.POST.get('registerUsername')
        password = request.POST.get('registerPasswords')
        user = User.objects.create_user(username=username, password=password)
        userprofile = UserProfile(user=user, name=username)
        userprofile.save()
        login(request, user)
        return redirect('/')
    return render(request, 'bbs/register.html')


# 版块页
def category(request):
    category_list = Category.objects.all()
    return render(request, 'bbs/category.html', locals())


# 版块详情页
def caregorydetail(request):
    category_name = request.GET.get('name')
    category_detail = Category.objects.get(name=category_name)
    post_list = Post.objects.filter(category_id=category_detail.pk)
    return render(request, 'bbs/caregorydetail.html', locals())


# 帖子详情页
def postdetail(request, post_id):
    post = Post.objects.get(id=post_id)
    post_content_type = ContentType.objects.get_for_model(post)
    comments = Comment.objects.filter(content_type=post_content_type, object_id=post_id)
    return render(request, 'bbs/postdetail.html', locals())


# 发表帖子
def publish(request):
    category_list = Category.objects.all()
    if request.method == 'POST':
        post_category = request.POST.get('post-category')
        post_theme = request.POST.get('post-theme')
        title = request.POST.get('post-title')
        post_content = request.POST.get('post-content')
        user_id = request.user.id
        post = Post()
        post.category = Category.objects.get(id=post_category)
        post.theme = Theme.objects.get(name=post_theme)
        post.title = title
        post.content = post_content
        post.author = UserProfile.objects.get(id=user_id)
        post.save()
        return HttpResponseRedirect('/')

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