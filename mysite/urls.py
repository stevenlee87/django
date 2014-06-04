from django.conf.urls import *
from mysite.views import hello

urlpatterns = patterns('',
    ('^hello/$', hello),
)
