from django import template
from django.utils.html import format_html

register = template.Library()

@register.filter(name='cut_page')
def cut_page(cur_page,val):

    val = int(val)
    if cur_page-val > 0:
        return range(cur_page-val,cur_page+val+1)
    else:
        return range(1,6)

@register.filter(name='cut2_page')
def cut2_page(page,val):

    val = int(val)
    if page[2]+2 > val:
        return range(val-4,val+1)
    else:
        return page

@register.filter(name='gt')
def gt(val1,val2):
    val2 = int(val2)
    if val1>val2:
        return 1
    else:
        return 0
