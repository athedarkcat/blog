# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *

# Create your views here.

def navPage(request):

	navs = Nav.objects.all()
	content = {'navs':navs}
	return render(request,'navigation/nav.html',content)
