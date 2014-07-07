from django.conf.urls import *
from mysite.views import hello, current_datetime, hours_ahead, current_url_view_good, display_meta
#from mysite.views import *
from django.contrib import admin
from books import views
admin.autodiscover()


urlpatterns = patterns('',
    ('^hello/$', hello),
    ('^time/$', current_datetime),
    ('^time/plus/(\d{1,2})/$', hours_ahead),
    ('^admin/', include(admin.site.urls)),
	('^current/$', current_url_view_good),
	('^display_meta/$', display_meta),
	('^search-form/$', views.search_form),
	('^search/$', views.search),
)
