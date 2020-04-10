from django import template

register = template.Library()


@register.filter
def info_is_none(obj):
    if obj is None:
        return ''
    else:
        return obj


@register.filter
def info_gender(obj):
    if obj is None:
        return ''
    elif obj == 1:
        return '男'
    elif obj == 0:
        return '女'


