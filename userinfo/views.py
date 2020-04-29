import time

from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from bbs.models import UserProfile, Post
# Create your views here.
from likes.models import LikeCount


def userinfo(request):
    name = request.GET.get('name')
    page = request.GET.get('page')
    user_info = UserProfile.objects.get(name=name)
    post_list = user_info.post_set.all()
    hot_post = user_info.post_set.all().order_by('-read_num')[:3]
    liked_count = 0
    for i in post_list:
        content_type = ContentType.objects.get_for_model(i)
        like_count, created = LikeCount.objects.get_or_create(content_type=content_type, object_id=i.id)
        liked_count += like_count.liked_num
    if page:
        new_page = int(page) - 1
    if request.is_ajax():
        return render(request, 'userinfo/user_info_post.html', locals())
    return render(request, 'userinfo/userinfo.html', locals())


def modify_img(request):
    if request.method == 'POST':
        file = request.FILES.get('img_file')
        file_name = request.POST.get('img_name').rsplit('.', 1)
        file_path = file_name[0] + str(time.time()) + '.' + file_name[-1]
        with open('media/head_img/'+file_path, 'wb') as f:
            for chunk in file.chunks():
                f.write(chunk)
        user = request.user.userprofile
        user.image = file_path
        user.save()
        return HttpResponse('修改成功')

def modify_info(request):
    if request.method == 'POST':
        username = request.POST.get('userprofile')
        nickname = request.POST.get('nickname')
        signature = request.POST.get('signature')
        gender = request.POST.get('gender')
        grade = request.POST.get('grade')
        college = request.POST.get('college')
        user = UserProfile.objects.get(name=username)
        user.name = nickname
        user.signature = signature
        user.gender = gender
        user.grade = grade
        user.college = college
        user.save()
        return JsonResponse({'status': 200})

def del_post(request):
    post_id = request.GET.get('post')
    Post.objects.get(id=post_id).delete()
    return JsonResponse({'status': 200})
