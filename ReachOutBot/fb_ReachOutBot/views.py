from django.shortcuts import render

# Create your views here.

from django.views import generic
from django.http.response import HttpResponse

class ReachOutBotView(generic.View):
    def get(self, request, *args, **kwArgs):
        return HttpResponse("Hi!")
