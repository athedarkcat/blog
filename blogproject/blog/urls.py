from django.conf.urls import include, url
import views


urlpatterns = [
    url(r'^blog/$',views.BlogView.as_view(),name='blog'),
    url(r'^about/$',views.aboutPage,name='about'),
    url(r'^blog/filter/$',views.BlogFilterView.as_view(),name='blogfilter'),
]
