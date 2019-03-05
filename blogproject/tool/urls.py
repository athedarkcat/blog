from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'sign/',view=signInPage,name='sign'),
    url(r'login/',view=login,name='login'),
    url(r'tool/',view=toolPage,name='toolpage'),
    url(r'exit/',view=exit,name='exit'),
]
