# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Nav(models.Model):

    title = models.CharField(max_length=50)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    link = models.CharField(max_length=100,blank=True,null=True)


    def __str__(self):
        return self.title
