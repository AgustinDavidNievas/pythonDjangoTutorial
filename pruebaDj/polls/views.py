from django.shortcuts import render
from django.http import HttpResponse
from django.template.context_processors import request

from polls.models import Poll#Mismo detalle del path que eclipse no se da cuenta pero por la consola funciona :P
#from pruebaDj.polls.models import Poll

# Create your views here.
def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    output = ', '.join([p.question for p in latest_poll_list])
    return HttpResponse(output)

def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)