# Create your views here.
from django.shortcuts import render, HttpResponse
from django.core.wsgi import get_wsgi_application

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from json import loads, dumps

#import MySQLdb
import json
import requests

from datetime import date
from comm.models import equipment
import re

import pymysql
import sys

DB_NAME = "db_name"
DB_TABLE = "db_table"

lowerRegex = re.compile('[a-z]')
upperRegex = re.compile('[A-Z]')
digitRegex = re.compile('[0-9]')
wrongRegex = re.compile('[^a-zA-Z0-9]')

def index(request):
    #try:
        conn = pymysql.connect(host='localhost',user='root',password='qes4812',charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        conn_talk = "CREATE DATABASE IF NOT EXISTS %s"
        cursor.execute(conn_talk % DB_NAME)
        conn_talk = "USE %s"
        cursor.execute(conn_talk % DB_NAME)				
        cursor.execute('CREATE TABLE IF NOT EXISTS %s(id int not null auto_increment primary key,name varchar(30))' % DB_TABLE)		
        conn_talk = "SELECT * FROM %s"
        cursor.execute(conn_talk % DB_TABLE)
        fetdata = cursor.fetchall()	
        cursor.close()
        conn.close()
        return render(request, 'database/index.html', {'db_table': "db_table", 'db_lists': fetdata})
    #except:
     #   return HttpResponse("index erro web!")	 
	
def add_database(request):
    try:
        if request.method == "GET":
            return render(request, 'database/index.html')
            #return HttpResponse("get web!")
        elif request.method == "POST":
            add_db_name = request.POST.get('add_db_name')
            while True:
                if len(add_db_name) <= 3 or len(add_db_name) >= 20:
                    return HttpResponse("input len is fail!",add_db_name)
                elif wrongRegex.search(add_db_name) != None:
                    return HttpResponse("input is fail!")
                elif lowerRegex.search(add_db_name) == None and upperRegex.search(add_db_name) == None:
                    return HttpResponse("input is null!")
                else:				
                    con = pymysql.connect(host='localhost', user='root',passwd='qes4812', charset='utf8')
                    cur = con.cursor(cursor=pymysql.cursors.DictCursor) 	
                    sql_talk="CREATE DATABASE IF NOT EXISTS %s"
                    cur.execute(sql_talk % add_db_name)	
                    # Write the db name to database
                    sql_talk = "USE %s"
                    cur.execute(sql_talk % DB_NAME)	
                    sql_talk = 'INSERT INTO db_table(name) VALUES(%s);'
                    cur.execute(sql_talk, [add_db_name])
                    con.commit()
                    cur.close()
                    con.close() 
                    return HttpResponseRedirect('/database/index')
        else:
             return HttpResponse("else web!")
    except:
        return HttpResponse("add_database erro web!")	 
		
def del_database(request, name):
    try:			
        del_con = pymysql.connect(host='localhost', user='root',passwd='qes4812', charset='utf8')
        del_cursor = del_con.cursor()	
        del_talk="DROP DATABASE IF EXISTS %s"
        del_cursor.execute(del_talk % name)
        del_talk="USE %s"
        del_cursor.execute(del_talk % DB_NAME)		
        # Delete the db name to database
        del_talk="DELETE FROM db_table WHERE name = '%s'"
        del_cursor.execute(del_talk % name)	
        del_con.commit()
        del_cursor.close()
        del_con.close()
		
        return HttpResponseRedirect('/database/index')
    except:
        return HttpResponse("del_database is fail!")
				
def show_table(request, name):
    try:
        show_table_con = pymysql.connect(host='localhost', user='root',passwd='qes4812', charset='utf8')
        show_table_cursor = show_table_con.cursor()
        show_talk = "USE %s"
        show_table_cursor.execute(show_talk % name)	
        show_table_cursor.execute("SHOW TABLES;")
        show_table_data = show_table_cursor.fetchall()
        show_db_list = []
        for j in range(len(show_table_data)):
            show_db_list.append(show_table_data[j][0])
        show_table_cursor.close()
        show_table_con.close()		
        return render(request, 'database/index.html', {'show_table': "show_table", 'table_lists': show_db_list, 'show_db_name': name})		
    except:
        return HttpResponse("show_table web fail!")

def add_table(request, table):
    try:
        add_table_name = request.POST.get('add_table_name')	
        add_table_con = pymysql.connect(host='localhost', user='root',passwd='qes4812', charset='utf8')
        add_table_cursor = add_table_con.cursor()	
        add_talk = "USE %s"
        add_table_cursor.execute(add_talk % table)		
        add_table_cursor.execute('CREATE TABLE IF NOT EXISTS %s(id int not null auto_increment primary key,name varchar(30))' % add_table_name)
        add_table_cursor.execute("SHOW TABLES;")
        add_table_data = add_table_cursor.fetchall()
        add_db_list = []
        for k in range(len(add_table_data)):
            add_db_list.append(add_table_data[k][0])
        add_table_cursor.close()
        add_table_con.close()			
        return render(request, 'database/index.html', {'show_table': "show_table", 'table_lists':add_db_list, 'show_db_name': table})
    except:
        return HttpResponse("add_table web fail!")				
		 
def del_table(request, name, table):
    try:
        del_table_con = pymysql.connect(host='localhost', user='root',passwd='qes4812', charset='utf8')
        del_table_cursor = del_table_con.cursor()		
        del_talk = "USE %s"
        del_table_cursor.execute(del_talk % name)			
        del_talk = "DROP TABLE IF EXISTS %s"
        del_table_cursor.execute(del_talk % table)	
        del_table_cursor.execute("SHOW TABLES;")
        del_table_data = del_table_cursor.fetchall()
        del_db_list = []
        for i in range(len(del_table_data)):
            del_db_list.append(del_table_data[i][0])
        del_table_con.commit()		
        del_table_cursor.close()
        del_table_con.close()
 
        return render(request, 'database/index.html', {'show_table': "show_table", 'table_lists':del_db_list, 'show_db_name': name})
    except:
        return HttpResponse("del table web fail!")
#('id', 'int(11)', 'NO', 'PRI', None, 'auto_increment')('name', 'varchar(30)', 'YES', '', None, '')
def show_column(request, name, table):
    #try:
        show_column_con = pymysql.connect(host='localhost', user='root',passwd='qes4812', charset='utf8')
        show_column_cursor = show_column_con.cursor()		
        show_column_talk = "USE %s"
        show_column_cursor.execute(show_column_talk % name)	
        show_column_talk = "DESC %s"
        show_column_cursor.execute(show_column_talk % table)	
        show_column_data = show_column_cursor.fetchall()
        show_column_list = []
        for m in range(len(show_column_data)):
            {
            show_column_list.append(show_column_data[m][0])
            }
        show_column_cursor.close()
        show_column_con.close()		
        return render(request, 'database/index.html', {'show_column': "show_column", 'show_db_name': name, 'show_table_name': table, 'column_lists':show_column_list})
    #except:
    #    return HttpResponse("del table web fail!")		

def add_column_char(request, name, table):
    #try:
        col_path = request.get_full_path()
        col_path = col_path.split('/')
        #return HttpResponse(col_path[3])
        add_column_name = request.POST.get('add_cloumn_name') 
        add_column_con = pymysql.connect(host='localhost', user='root',passwd='qes4812', charset='utf8')
        add_column_cursor = add_column_con.cursor()		
        add_column_talk = "USE %s"
        add_column_cursor.execute(add_column_talk % col_path[2])
        add_column_talk = "ALTER TABLE %s ADD %s varchar(50)"
        add_column_cursor.execute(add_column_talk % (col_path[3],add_column_name))
        add_column_talk = "DESC %s"
        add_column_cursor.execute(add_column_talk % col_path[3])	
        add_column_data = add_column_cursor.fetchall()
        add_column_list = []
        for m in range(len(add_column_data)):
            add_column_list.append(add_column_data[m][0])
        add_column_cursor.close()
        add_column_con.close()		
        return render(request, 'database/index.html', {'show_db_name': col_path[2], 'show_table_name': col_path[3], 'show_column': "show_column", 'column_lists':add_column_list})
    #except:
     #   return HttpResponse("add column web fail!")		

def add_column_num(request, name, table):
    #try:
        col_path = request.get_full_path()
        col_path = col_path.split('/')
        #return HttpResponse(col_path[3])
        add_column_name = request.POST.get('add_cloumn_name') 
        add_column_con = pymysql.connect(host='localhost', user='root',passwd='qes4812', charset='utf8')
        add_column_cursor = add_column_con.cursor()		
        add_column_talk = "USE %s"
        add_column_cursor.execute(add_column_talk % col_path[2])
        add_column_talk = "ALTER TABLE %s ADD %s decimal(20)"
        add_column_cursor.execute(add_column_talk % (col_path[3],add_column_name))
        add_column_talk = "DESC %s"
        add_column_cursor.execute(add_column_talk % col_path[3])	
        add_column_data = add_column_cursor.fetchall()
        add_column_list = []
        for m in range(len(add_column_data)):
            add_column_list.append(add_column_data[m][0])
        add_column_cursor.close()
        add_column_con.close()		
        return render(request, 'database/index.html', {'show_db_name': col_path[2], 'show_table_name': col_path[3], 'show_column': "show_column", 'column_lists':add_column_list})
    #except:
     #   return HttpResponse("add column web fail!")	

def del_column(request, name, table, column):
    #try:
        del_column_con = pymysql.connect(host='localhost', user='root',passwd='qes4812', charset='utf8')
        del_column_cursor = del_column_con.cursor()		
        del_column_talk = "USE %s"
        del_column_cursor.execute(del_column_talk % name)
        del_column_talk = "ALTER TABLE %s DROP COLUMN %s"
        del_column_cursor.execute(del_column_talk % (table,column))
        del_column_talk = "DESC %s"
        del_column_cursor.execute(del_column_talk % table)	
        del_column_data = del_column_cursor.fetchall()
        del_column_list = []
        for k in range(len(del_column_data)):
            del_column_list.append(del_column_data[k][0])
        del_column_cursor.close()
        del_column_con.close()		
        return render(request, 'database/index.html', {'show_db_name': name, 'show_table_name': table, 'show_column': column, 'column_lists':del_column_list})
        return HttpResponse(name)
    #except:
     #   return HttpResponse(del column web fail!")	

def modify_column(request):
        return HttpResponse("modify_column web!")		
		
def backup_all_database(request):
        return HttpResponse("backup_all_database web!")

def backup_database(request):
        return HttpResponse("backup_database web!")	
