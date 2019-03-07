# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from .models import *


# Create your views here.

def toolPage(request):

    tools = Tool.objects.all()
    content = {
        'tools':tools,
    }
    return render(request,'tool/tool.html',content)
