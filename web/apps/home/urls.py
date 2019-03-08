from django.urls import path,re_path
from . import views

urlpatterns = [
        path('',             views.index,        name='index'),
        path('index',        views.index,        name='index'),
        path('stock',        views.stock,        name='stock'),
        path('add_stock',    views.add_stock,    name='add_stock'),
        re_path('delete_stock/(?P<id>[0-9]+)', views.delete_stock, name='delete_stock'),
        re_path('modify_stock/(?P<id>[0-9]+)', views.modify_stock, name='modify_stock')
]
