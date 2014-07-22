from django.conf import settings
from django.http import HttpResponse
from django.utils.importlib import import_module
from django.shortcuts import render_to_response
#import gdata.docs.service
players_details = [ ('a',32,'Right Hand Bat' ),  ]
from django.shortcuts import render
def index(request):
    content_type = 'text/plain; charset=%s' % settings.DEFAULT_CHARSET
    return HttpResponse("Warmup done.", content_type=content_type)

def scorecard( request ):
    return render_to_response('mainapp/scorecard.html')

def getBattingScGridData( request):
    return render(request, 'mainapp/battinggriddata.xml', {"foo": "bar"}, content_type="application/xhtml+xml")

def getBowlingScGridData( request):
    return render(request, 'mainapp/bowlinggriddata.xml', {"foo": "bar"}, content_type="application/xhtml+xml")

def practice( request ):
    return render_to_response('mainapp/practice.html')

def availability( request ):
    return render_to_response('mainapp/availability.html')

def about( request ):
    return render_to_response('mainapp/about.html')

def join( request ):
    return render_to_response('mainapp/join.html')

