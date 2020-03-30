import time

from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from bbs.models import UserProfile
# Create your views here.


def userinfo(request):
    name = request.GET.get('name')
    user_info = UserProfile.objects.get(name=name)
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

