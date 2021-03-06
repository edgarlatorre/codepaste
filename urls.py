from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^codepaste/', include('codepaste.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
	url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	url(r'^$', 'codepaste.paste.views.index', name='index'),
	url(r'^code/save$', 'codepaste.paste.views.save', name='save'),
	url(r'^code/(?P<slug>[\w_-]+)/$', 'codepaste.paste.views.show', name='show'),
)
