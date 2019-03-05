# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Tool(models.Model):

    title = models.CharField(max_length=100,null=False)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    local_link = models.CharField(max_length=200,blank=True,null=True)
    extral_link = models.CharField(max_length=200,blank=True,null=True)

class User(models.Model):

    uuid = models.CharField(max_length=50)
    upwd = models.CharField(max_length=50)
    upermission = models.CharField(max_length=5,default='1')
