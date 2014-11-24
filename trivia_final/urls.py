from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'trivia_final.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include("trivia_final.apps.principal.urls")),
    url(r'^user/', include("trivia_final.apps.usuario.urls")),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)