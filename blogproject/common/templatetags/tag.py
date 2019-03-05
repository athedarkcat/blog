from django import template
from django.utils.html import format_html

register = template.Library()

@register.filter(name="str_split")
def str_split(str1,separator):
    if not str1:
        return ''
    else:
        tmp = str1.split(separator)
        return tmp

@register.filter(name="list_index")
def list_index(lt,index):
    if not lt:
        return ''
    else:
        index = int(index)
        return lt[index]
