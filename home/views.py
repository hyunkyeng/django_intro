from django.shortcuts import render, HttpResponse
from pprint import pprint
import random

# Create your views here.
def index(request):
    return HttpResponse('Welcome to Django!')
    
def dinner(request):
    menus = ['베이컨버거', '페퍼로니피자', '쌀국수', '떡볶이', 'sushi']
    pick = random.choice(menus)
    # return HttpResponse(menu) #서버에서 열리는 방법
    return render(request, 'dinner.html', {'menus': menus, 'pick': pick} ) #dinner.html 에서 열리는 방법 
    
def hello(request, name):
    return render(request, 'hello.html', {'name': name})
    
def cube(request, number):
    num = number ** 3
    return render(request, 'cube.html', {'number': number, 'num': num})