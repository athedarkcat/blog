# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from .models import *


# Create your views here.

def signInPage(request):

    return render(request,'tool/sign.html')

def toolPage(request):

    tools = Tool.objects.all()
    content = {
        'tools':tools,
    }
    return render(request,'tool/tool.html',content)

def login(request):

    if request.method=='POST':
        if request.POST['uid']=='user' and request.POST['pwd']=='123456':
            request.session["login_status"] = "1"
            return redirect('/tool/tool/')
        else:
            return HttpResponse('密码错误')
    else:
        return HttpResponse('错误')

def exit(request):

    del request.session['login_status']
    return redirect('/tool/sign')
