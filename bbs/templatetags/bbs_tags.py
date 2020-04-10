import random
from django import template
from django.contrib.contenttypes.models import ContentType

from likes.models import LikeCount

register = template.Library()
@register.simple_tag
def get_label():
    lst = ['label-default','label-primary','label-success','label-info','label-warning']
    return random.choice(lst)
@register.simple_tag
def get_like_user(obj):
    liked_count = 0
    for i in obj:
        content_type = ContentType.objects.get_for_model(i)
        like_count, created = LikeCount.objects.get_or_create(content_type=content_type, object_id=i.id)
        liked_count += like_count.liked_num
    return liked_count
