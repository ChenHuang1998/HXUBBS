# import requests
# from lxml import etree
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from bbs.models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    category_list = Category.objects.all()
    post_list = Post.objects.all()
    return render(request, 'bbs/index.html', locals())


def acc_login(request):
    if request.method == "POST":
        user = authenticate(username=request.POST.get('username'),
                            password=request.POST.get('password'))
        if user:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            login_error = '用户名密码错误'
            return render(request, 'bbs/login.html',{'login_error': login_error})
    return render(request, 'bbs/login.html')


def acc_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def category(request):
    category_list = Category.objects.all()
    return render(request, 'bbs/category.html', locals())


def caregorydetail(request):
    category_name = request.GET.get('name')
    category_id = Category.objects.get(name=category_name).pk
    post_list = Post.objects.filter(category_id=category_id)

    return render(request, 'bbs/caregorydetail.html', locals())

# def addpost(request):
#     for i in range(6):
#         base_url = 'http://jianyuluntan.com/?order=&page={}'.format(i)
#         response = requests.get(base_url)
#         html_str = etree.HTML(response.text)
#         div_list = html_str.xpath('//div[@class="col-md-9"]/div[position()>1]')
#         for div in div_list:
#             title = div.xpath('./div/h6/a/text()|./div/h5/a[3]/text()')[0]
#             url = 'http://jianyuluntan.com'+div.xpath('./div/h6/a/@href|./div/h5/a[3]/@href')[0]
#             detail = requests.get(url)
#             detail_str = etree.HTML(detail.text)
#             content = detail_str.xpath('string(//div[@class="zhengwen"])').strip()
#             user = UserProfile.objects.first()
#             category = Category.objects.first()
#             post = Post()
#             post.title = title
#             post.content = content
#             post.author = user
#             post.category = category
#             post.save()
#     return HttpResponse('1')