from django.http import HttpResponse
from django.shortcuts import render
from .task import task_func
# Create your views here.

def home(request):
    task_func.delay()
    return HttpResponse('Done')