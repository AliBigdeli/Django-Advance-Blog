from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core.cache import cache
import time 
from .tasks import sendEmail
import requests

def send_email(request):
    sendEmail.delay()
    return HttpResponse("<h1>Done Sending</h1>")

def test(request):
    if cache.get("test_delay_api") is None:
        response = requests.get("https://b0334311-3948-4555-af18-17d55a318926.mock.pstmn.io/test/delay/5")
        cache.set("test_delay_api",response.json(),60)
    return JsonResponse(cache.get("test_delay_api"))
