from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'tasks.views.home', name='home'),
    url(r'^tasks/$', 'tasks.views.tasks', name='tasks'),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

)

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', 
    	{'document_root': settings.STATIC_ROOT}))

