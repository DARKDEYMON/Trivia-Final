from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'trivia_final.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', vista_principal, name="home"),
)
