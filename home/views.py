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

#get 형식으로 핑퐁
def ping(request):
    return render(request, 'ping.html')
    
def pong(request):
    print(request.GET)
    data = request.GET.get('data')
    return render(request, 'pong.html', {'data': data})

#post 형식으로 핑퐁
def user_new(request):
    return render(request, 'user_new.html')
    
def user_create(request):
    nickname = request.POST.get('nickname')
    pwd = request.POST.get('pwd')
    return render(request, 'user_create.html', {'nickname': nickname, 'pwd': pwd})