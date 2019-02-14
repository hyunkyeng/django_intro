from django.shortcuts import render
from datetime import datetime, timedelta
import requests, os, json

# Create your views here.
def index(request):
    return render(request, 'utilities/index.html')
    
def bye(request):
    bye_time = datetime(2019, 2, 28)
    time = (bye_time - datetime.now()) // timedelta(days=1)
    return render(request, 'utilities/bye.html', {'time':time})
    
def graduation(request):
    grad = datetime(2019, 5, 28)
    grad_time = (grad - datetime.now()) // timedelta(days=1)
    return render(request, 'utilities/graduation.html', {'grad_time':grad_time})
    
def imagepick(request):
    return render(request, 'utilities/imagepick.html')
    
def today(request):
    key = os.getenv('WEATHER_KEY')
    print(key)
    url = f'https://api.openweathermap.org/data/2.5/weather?q=Daejeon,kr&lang=kr&APPID={key}'
    req = requests.get(url).json()
    time = datetime.now()
    weather = req['weather'][0]['description']
    temp = round(req['main']['temp'] - 273.15, 2)
    temp_min = req['main']['temp_min'] - 273.15
    temp_max = req['main']['temp_max'] - 273.15
    return render(request, 'utilities/today.html', {'time': time, 'weather': weather, 'temp': temp, 'temp_min': temp_min, 'temp_max': temp_max})
    
def ascii_new(request):
    fonts = ['short', 'utopia', 'rounded', 'acrobatic', 'alligator']
    return render(request, 'utilities/ascii_new.html', {'fonts': fonts})
    
def ascii_make(request):
    text = request.GET.get('text')
    font = request.GET.get('font')
    url = f'http://artii.herokuapp.com/make?text={text}&font={font}'
    req = requests.get(url).text
    return render(request, 'utilities/ascii_make.html', {'req': req})
    
def original(request):
    return render(request, 'utilities/original.html')

def translated(request):
    naver_client_id = os.getenv("NAVER_ID")
    naver_client_secret = os.getenv("NAVER_SECRET")
    print(naver_client_id, naver_client_secret)
    papago_url = "https://openapi.naver.com/v1/papago/n2mt"
    text = request.POST.get('text')
    
    headers = {
    "X-Naver-Client-Id": naver_client_id,
    "X-Naver-Client-Secret": naver_client_secret
    }
    data = {
    "source": "ko",
    "target": "en",
    "text": text
    }
    papago_response = requests.post(papago_url, headers=headers, data=data).json()
    print(papago_response)
    reply_text = papago_response["message"]["result"]["translatedText"]
    
    return render(request, 'utilities/translated.html', {'reply_text': reply_text})
    
    