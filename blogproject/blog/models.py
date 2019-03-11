# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class PersonLink(models.Model):
    """友情链接"""

    name = models.CharField('链接名称',max_length=100)
    sequence = models.IntegerField('排序', unique=True)
    created_time = models.DateTimeField('创建时间',auto_now_add=True)
    modified_time = models.DateTimeField('修改时间',auto_now=True)
    link = models.URLField('链接地址')

    class Meta:
        ordering = ['sequence']

    def __unicode__(self):
        return self.name

class Article(models.Model):
    """文章"""

    STATUS_CHOICES = (
        ('d', '草稿'),
        ('p', '发表'),
    )
    title = models.CharField('标题', max_length=200, unique=True)
    body = models.TextField('正文')
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField('浏览量', default=0)
    article_order = models.IntegerField('排序,数字越大越靠前', blank=False, null=False, default=0)
    category = models.ForeignKey('Category', verbose_name='分类', on_delete=models.CASCADE, blank=False, null=False)
    tags = models.ManyToManyField('Tag', verbose_name='标签集合', blank=True)

    class Meta:
        ordering = ['-article_order', '-modified_time']

    def __unicode__(self):
        return self.title

class Category(models.Model):
    """文章分类"""

    name = models.CharField('分类名', max_length=30, unique=True)
    parent_category = models.ForeignKey('self', verbose_name="父级分类", blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

class Tag(models.Model):
    """文章标签"""

    name = models.CharField('标签名', max_length=30, unique=True)

    def __unicode__(self):
        return self.name
