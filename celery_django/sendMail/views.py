import imp
from django.shortcuts import render
from django.http import HttpResponse
from sendMail.task import send_mail_to_all
# Create your views here.

def send_mail(request):
    send_mail_to_all.delay()
    return HttpResponse('Done')
