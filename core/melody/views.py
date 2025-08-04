from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def melody_home(request):
    return HttpResponse("This is Home for melody Songs")