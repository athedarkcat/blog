from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'tool/',view=toolPage,name='toolpage'),
]
