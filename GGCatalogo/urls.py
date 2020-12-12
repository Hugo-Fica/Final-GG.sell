from django.conf import settings
from django.urls.conf import path
from django.urls import re_path
from . import views
from django.conf.urls.static import static


urlpatterns = [
    re_path(r'^$', views.index, name="index"), # función url -> re_path
    re_path(r'^juegos/$', views.JuegoListView.as_view(), name='juegos'),
    re_path(r'^juegos/(?P<pk>\d+)$', views.JuegoDetailView.as_view(), name='juegos_detail'),
    re_path(r'^desarrolladores/$', views.DesarrolladorListView.as_view(), name='desarrolladores'),
    re_path(r'^desarrolladores/(?P<pk>\d+)$', views.DesarrolladorDetailView.as_view(), name='desarrollador_detail'),
   
]

