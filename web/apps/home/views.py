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

def index(request):
        addarticle=equipment()
        stock_db=equipment.objects.all()
        return render(request, 'home/index.html', {'stock_db':stock_db})

def stock(request):
        return HttpResponse("stock web")
		
def add_stock(request):
        return HttpResponse("add stock web")	

def delete_stock(request, id):
        del_stock=equipment.objects.get(id=int(id))
        del_stock.delete()
        return HttpResponseRedirect('/home/index')
		#return HttpResponse("delete stock web")	
	
def modify_stock(request, id):
        mdf_stock=equipment.objects.get(id=int(id))
        mdf_stock.name='mean'
        mdf_stock.option='mean'
        mdf_stock.save()
        #return HttpResponseRedirect('/home/stock')
        #return render(request,"home/stock.html")
        return HttpResponse("modify stock web")		
