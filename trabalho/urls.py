# from django.conf.urls import url
# from . import views
#
# app_name = 'trabalho'
#
# urlpatterns = [
#     # ex: /trabalho/
#     url(r'^$', views.index, name='index'),
#     # ex: /trabalho/5/
#     url(r'^detalhes/(?P<pergunta_id>[0-9]+)/$', views.detalhe, name='detalhe'),
#     # ex: /trabalho/5/resultados/
#     url(r'^(?P<pergunta_id>[0-9]+)/resultados/$', views.resultados, name='resultados'),
#     # ex: /trabalho/5/voto/
#     url(r'^(?P<pergunta_id>[0-9]+)/voto/$', views.voto, name='voto'),
# ]

from django.conf.urls import url
from . import views

app_name = 'trabalho'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^cadastro/$', views.cadastro, name='cadastro'),
    url(r'^menu/$', views.menu, name='menu'),
    url(r'^footer/$', views.footer, name='footer'),
    url(r'^shows/show/(?P<show_id>[0-9]+)/$', views.mostrarShow, name='show'),
    url(r'^shows/show/alterar/$', views.alterar, name='alterar'),
    url(r'^shows/show/remover/$', views.remover, name='remover'),
    url(r'^shows/$', views.ListaDeShows.as_view(), name='lista'),
]
