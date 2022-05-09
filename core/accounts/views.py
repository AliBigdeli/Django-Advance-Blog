from django.shortcuts import render
from django.http import HttpResponse
import time 
from .tasks import sendEmail


def send_email(request):
    sendEmail.delay()
    return HttpResponse("<h1>Done Sending</h1>")
