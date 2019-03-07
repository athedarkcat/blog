# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.

def blogPage(request):

    return render(request,'blog/blog.html')

def aboutPage(request):

    return render(request,'blog/about.html')
