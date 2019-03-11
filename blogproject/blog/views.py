# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404

from django.shortcuts import render
from django.http import HttpResponse
from blog.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView
import random

# Create your views here.

class BlogView(ListView):
    model = Article
    template_name = 'blog/blog.html'
    context_object_name = 'articles'

    def get_context_data(self,**kwargs):
        context = super(BlogView,self).get_context_data(**kwargs)
        personlinks = PersonLink.objects.all()
        cateSum = len(Category.objects.all())
        if cateSum > 5:
            numRadom = random.randint(0,cateSum-5)
            context['cates'] = Category.objects.all()[numRadom:numRadom+4]
        else:
            context['cates'] = Category.objects.all()
        context['personlinks'] = personlinks
        return context

    def get_queryset(self):

        tmp = Article.objects.all().all()
        paginator = Paginator(tmp, 3) # 每页显示25条
        page = self.request.GET.get('page')
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            # 如果请求的页数不是整数，返回第一页。
            articles = paginator.page(1)
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            articles = paginator.page(paginator.num_pages)
        return articles

class BlogFilterView(BlogView):

    def get_queryset(self):

        cate_id = 2
        tmp = Article.objects.filter(category__id__contains=int(cate_id))
        paginator = Paginator(tmp, 3) # 每页显示25条
        page = self.request.GET.get('page')
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            # 如果请求的页数不是整数，返回第一页。
            articles = paginator.page(1)
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            articles = paginator.page(paginator.num_pages)
        return articles


def blogPage(request):

    cateSum = len(Category.objects.all())
    if cateSum > 5:
        numRadom = random.randint(0,cateSum-5)
        cates = Category.objects.all()[numRadom:numRadom+4]
    else:
        cates = Category.objects.all()

    personlinks = PersonLink.objects.all()
    articles = Article.objects.all().all()
    paginator = Paginator(articles, 4) # 每页显示25条
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果请求的页数不是整数，返回第一页。
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
        contacts = paginator.page(paginator.num_pages)
    content = {
        'cates':cates,
        'articles':contacts,
        'personlinks':personlinks,
    }

    return render(request,'blog/blog.html',content)

def aboutPage(request):

    personlinks = PersonLink.objects.all()
    content = {
        'personlinks':personlinks,
    }

    return render(request,'blog/about.html',content)

# def articleFilter(request):
#
#     return
