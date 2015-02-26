from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'async.views.home', name='home'),
    url(r'^get_data$', 'async.views.get_data'),
    url(r'^admin/', include(admin.site.urls)),
)
