from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse
from likes.models import *
# Create your views here.


def like_change(request):
    content_type = request.GET.get('content_type')
    content_type = ContentType.objects.get(model=content_type)
    object_id = request.GET.get('object_id')
    is_like = request.GET.get('is_like')
    user = request.user

    if user.is_anonymous:
        return JsonResponse({'status': 400, 'message': '未登录'})
    if is_like == 'true':
        # 点赞
        like_record, created = LikeRecord.objects.get_or_create(content_type=content_type, object_id=object_id, user=user.userprofile)
        if created:
            # 为点赞过
            like_count, created = LikeCount.objects.get_or_create(content_type=content_type, object_id=object_id)
            like_count.liked_num += 1
            like_count.save()
            return JsonResponse({'status': 200, 'like_num': like_count.liked_num})

        else:
            # 已点赞过
            return JsonResponse({'status': 401})

    else:
        # 取消点赞
        if LikeRecord.objects.filter(content_type=content_type, object_id=object_id, user=user.userprofile).exists():
            like_record = LikeRecord.objects.get(content_type=content_type, object_id=object_id, user=user.userprofile)
            like_record.delete()
            # 点赞总数减1
            like_count, created = LikeCount.objects.get_or_create(content_type=content_type, object_id=object_id)
            if not created:
                like_count.liked_num -= 1
                like_count.save()
                return JsonResponse({'status': 200, 'like_num': like_count.liked_num})
            else:
                return JsonResponse({'status':404})

        else:
            # 没有点赞过
            return JsonResponse({'status':403})


def unlike_change(request):
    pass