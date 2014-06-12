from django.conf.urls import *
from mysite.views import hello, current_datetime, hours_ahead

urlpatterns = patterns('',
    ('^hello/$', hello),
    ('^time/$', current_datetime),
    ('^time/plus/(\d{1,2})$', hours_ahead),
)
