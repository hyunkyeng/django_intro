from django.shortcuts import render, HttpResponse
from pprint import pprint

# Create your views here.
def index(request):
    return HttpResponse('Welcome to Django!')