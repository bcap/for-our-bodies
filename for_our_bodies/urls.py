from django.conf.urls import patterns, include, url
from django.contrib import admin
from for_our_bodies import views

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', views.index, name='index'),
    url(r'^users$', views.users, name='users'),
    url(r'^(?P<userid>\d+)$', views.user_by_id, name='user_by_id'),
    url(r'^(?P<username>[a-zA-Z]\w+)$', views.user_by_name, name='user_by_name'),

    url(r'^admin/', include(admin.site.urls)),
)
