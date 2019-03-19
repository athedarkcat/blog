from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^blog/$',views.BlogView.as_view(),name='blog'),
    url(r'^about/$',views.aboutPage,name='about'),
    url(r'^blog/filter/(\w+)/(\d+)/$',views.BlogFilterView.as_view(),name='blogfilter'),
    url(r'^blog/article/(\d+)/$',views.ArticleView.as_view(),name='blogArticle'),
]
