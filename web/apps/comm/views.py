from django.shortcuts import render, HttpResponse
from django.core.wsgi import get_wsgi_application

# Create your views here.
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
        #addarticle.name='mean'
        #addarticle.option='mean'
        #addarticle.save()
        titles=equipment.objects.all()
        return render(request, 'comm/index.html', {'titles':titles})
        #return  HttpResponse("web")
       # context   =  {}
        #context['hello'] = 'Hello World!'
        #return render(request, 'comm/index.html', context)

def comm_process(request):                       
    resp = {'errorcode': 100, 'detail': 'Get success'}
    if request.method == 'GET':
        return HttpResponse(json.dumps(resp), content_type="application/json", status="201" )
    elif request.method == 'POST':
        story_data=request.body.decode('utf-8')
        story_data="".join(story_data.split())
        story_data=re.sub('"','',story_data)
        story_data=re.sub(':','=',story_data)
        #name=story_data.index('name')       
        #notes=story_data.index('notes')           
        name=re.findall(r"name=(\w+)",story_data)     
        option=re.findall(r"option=(\w+)",story_data)
        addarticle=equipment()

        addarticle.name="".join(name)
        addarticle.option="".join(option)
        addarticle.save()
        #return HttpResponse("Welcome to the page at %s" %story_data)
        return HttpResponseRedirect('/comm/index')

def addarticle(request):
        addarticle=equipment()
        addarticle.name='mean'
        addarticle.option='mean'
        addarticle.save()
        return HttpResponseRedirect('/comm/index')

def delarticle(request, id):
        dart=equipment.objects.get(id=int(id))
        dart.delete()
        return HttpResponseRedirect('/comm/index')

