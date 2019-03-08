from django.urls import path,re_path,reverse
from . import views

urlpatterns = [
        path('',                    views.index,               name='index'),
        path('add_database',        views.add_database,        name='add_database'),
        path('modify_column',       views.modify_column,       name='modify_column'),
        path('backup_all_database', views.backup_all_database, name='backup_all_database'),
        path('backup_database',     views.backup_database,     name='backup_database'),
        path('index',               views.index,               name='index'),
        re_path('(?P<table>(\w+))/add_table',   views.add_table,    name='add_table'),
        re_path('del_table/(?P<name>(\w+))/(?P<table>(\w+))',           views.del_table,           name='del_table'),
        re_path('show_table/(?P<name>(\w+))',    views.show_table,   name='show_table'),
        re_path('(?P<name>(\w+))/(?P<table>(\w+))/show_column',         views.show_column,         name='show_column'),
        re_path('(?P<name>(\w+))/(?P<table>(\w+))/add_column_char',          views.add_column_char,          name='add_column_char'),
        re_path('(?P<name>(\w+))/(?P<table>(\w+))/add_column_num',          views.add_column_num,          name='add_column_num'),
        re_path('(?P<name>(\w+))/(?P<table>(\w+))/(?P<column>(\w+))/del_column',          views.del_column,          name='del_column'),
        re_path('del_database/(?P<name>(\w+))', views.del_database, name='del_database')
]
