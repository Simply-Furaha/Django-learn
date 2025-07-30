from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def report_home(request):
    return HttpResponse("This is Just a Simple report page")