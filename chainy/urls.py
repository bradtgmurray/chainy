from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^chainy/', include('chainy.foo.urls')),
    (r'^$', 'chainy.chainyapp.views.main'),
    (r'^(?P<chain_id>\d+)/$', 'chainy.chainyapp.views.chain'),
    (r'^(?P<chain_id>\d+)/(?P<post_num>\d+)/$', 'chainy.chainyapp.views.post'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
)
