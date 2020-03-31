from django import template
from likes.models import *
from django.contrib.contenttypes.models import ContentType
register = template.Library()
@register.simple_tag
def get_like_count(obj):
    content_type = ContentType.objects.get_for_model(obj)
    like_count, created = LikeCount.objects.get_or_create(content_type=content_type, object_id=obj.id)
    return like_count.liked_num

@register.simple_tag(takes_context=True)
def get_like_status(context, obj):
    content_type = ContentType.objects.get_for_model(obj)
    user = context['user']
    if user.is_anonymous:
        return ''
    if LikeRecord.objects.filter(content_type=content_type, object_id=obj.id, user=user.userprofile).exists():
        return 'islike'
    else:
        return ''
