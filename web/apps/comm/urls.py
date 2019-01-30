from django.urls import path,re_path
from . import views

urlpatterns = [
        path('',             views.index,        name='index'),
        path('index',        views.index,        name='index'),
	path('comm_process', views.comm_process, name='comm_process'),
	path('addarticle', views.addarticle,     name='addarticle'),
        re_path('delarticle/(?P<id>[0-9]+)', views.delarticle, name='delarticle')
]
