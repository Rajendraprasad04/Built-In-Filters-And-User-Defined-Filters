from django import template
register=template.Library()
def swap(value):
    return value.swapcase()

register.filter('swapping',swap)
@register.filter('split')
def split(value,arg):
    return value.split(arg)
#register.filter('splitting',split)
@register.filter('index')
def index(value,i):
    return value.index(i)
@register.filter('find')
def find(value,i):
    return value.find(i)
@register.filter('append')
def append(value,arg):
    return value.append(arg)
