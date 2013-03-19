from django.conf.urls import patterns, include, url

from infodb.views import main
from infodb.views import logout_page
from infodb.views import edit

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', main),
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),
    url(r'^edit/(?P<person_id>\d+)$', edit),
    # Examples:
    # url(r'^$', 'infodbproject.views.home', name='home'),
    # url(r'^infodbproject/', include('infodbproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
