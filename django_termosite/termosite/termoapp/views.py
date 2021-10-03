from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Bb
 
def index(request):
    """КОНТРОЛЛЕР ФУНКЦИЯ index
    В ЕЕ ТЕЛЕ ЭКЗЕМПЛЯР КЛАССА HttpResponse
    """
    s = 'Список объявлений\r\n\r\n\r\n'

    #сортируем по убыванию по этому тут минус published
    for bb in Bb.objects.order_by('-published'):
        s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
        
    #return HttpResponse("Здесь будет список параметров датчика")
    return HttpResponse(s, content_type="text/plain; charset=utf-8")




