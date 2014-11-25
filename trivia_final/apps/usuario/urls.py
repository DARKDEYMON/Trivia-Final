from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'trivia_final.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^registro/', registro_view, name="registro"),
    url(r'^login/', login_view, name="login"),
    url(r'^logout/', logout_view, name="logout"),
    url(r'^actualisar/', actualisar_perfil_view, name="actualisar"),
    url(r'^tema/', temas_view, name="tema"),
    url(r'^crear_pregunta/', preguntas_view, name="preguntas"),
    url(r'^crear_respuestas/', respuestas_view, name="respuestas"),
    url(r'^lista_preguntas/', lista_preguntas_view, name="lista_preguntas"),
    url(r'^eliminar/(?P<id>.+?)/$', lista_preguntas_eliminar_view, name="eliminar"),
)