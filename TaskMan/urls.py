from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'tasks.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tasks/$', 'tasks.views.tasks', name='tasks'),
    url(r'^task/(?P<task_id>\d+)/$', 'tasks.views.task_detail',name='task')

)

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', 
    	{'document_root': settings.STATIC_ROOT}))

