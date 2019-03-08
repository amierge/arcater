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
        #addarticle=equipment()
        #addarticle.name='mean'
        #addarticle.option='mean'
        #addarticle.save()
        #titles=equipment.objects.all()
        #return render(request, 'comm/index.html', {'titles':titles})
        #return  HttpResponse("index web")
        context   =  {}
        context['hello'] = 'Hello World!'
        return render(request, 'index/index.html', context)
