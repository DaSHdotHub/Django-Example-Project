from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    if request.method == 'GET':
        return HttpResponse("GET World!")
    elif request.method == 'POST':
        return HttpResponse("POST World!")
    else:
        return HttpResponse("This is something else!")
