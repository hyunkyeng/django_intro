from django.shortcuts import render, HttpResponse
from pprint import pprint
import random
from datetime import datetime

# Create your views here.
def index(request):
    #return HttpResponse('Welcome to Django!')
    return render(request, 'home/index.html')
    
def dinner(request):
    menus = ['베이컨버거', '페퍼로니피자', '쌀국수', '떡볶이', 'sushi']
    pick = random.choice(menus)
    # return HttpResponse(menu) #서버에서 열리는 방법
    return render(request, 'home/dinner.html', {'menus': menus, 'pick': pick} ) #dinner.html 에서 열리는 방법 
    
def hello(request, name):
    return render(request, 'home/hello.html', {'name': name})
    
def cube(request, number):
    num = number ** 3
    return render(request, 'home/cube.html', {'number': number, 'num': num})

#get 형식으로 핑퐁
def ping(request):
    return render(request, 'home/ping.html')
    
def pong(request):
    print(request.GET)
    data = request.GET.get('data')
    return render(request, 'home/pong.html', {'data': data})

#post 형식으로 핑퐁
def user_new(request):
    return render(request, 'home/user_new.html')
    
def user_create(request):
    nickname = request.POST.get('nickname')
    pwd = request.POST.get('pwd')
    return render(request, 'home/user_create.html', {'nickname': nickname, 'pwd': pwd})
    
def template_example(request):
    my_list = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    empty_list = []
    datetimenow = datetime.now()
    return render(request, 'home/template_example.html',
                {'my_list': my_list, 'my_sentence': my_sentence, 'messages': messages, 'empty_list': empty_list, 'datetimenow': datetimenow})
                
def static_example(request):
    return render(request, 'home/static_example.html')