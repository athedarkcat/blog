# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *
from blog.models import PersonLink

# Create your views here.

def navPage(request):

	personlinks = PersonLink.objects.all()
	navs = Nav.objects.all()
	content = {
		'navs':navs,
		'personlinks':personlinks,
	}
	return render(request,'navigation/nav.html',content)
