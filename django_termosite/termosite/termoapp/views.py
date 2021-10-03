#from django import template
#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.template import loader

from .models import Bb, T_SBP_DBP_S_BR
 
def index(request):
    """КОНТРОЛЛЕР ФУНКЦИЯ index
    В ЕЕ ТЕЛЕ ЭКЗЕМПЛЯР КЛАССА HttpResponse
    """
    #s = 'Список объявлений\r\n\r\n\r\n'

    #сортируем по убыванию по этому тут минус published
    #for bb in Bb.objects.order_by('-published'):
    #    s += bb.title + '\r\n' + bb.content + '\r\n\r\n'

    #patients = 'Список пациентов\r\n\r\n\r\n'

    #сортируем по убыванию по этому тут минус published
    #for pp in T_SBP_DBP_S_BR.objects.order_by('-published'):
    #    patients += pp.title + '\r\n' + pp.sex + pp.temperature + pp.sbp + pp.dbp + pp.saturation + pp.breath_rate + '\r\n\r\n'

    #for pp in T_SBP_DBP_S_BR.objects.order_by('-published'):
    #    patients += pp.title + '\r\n' + pp.sex + '\r\n\r\n'
            
    #return HttpResponse("Здесь будет список параметров датчика")

    template = loader.get_template('termoapp/index.html')
    bbs = Bb.objects.order_by('-published')
    context = {'bbs': bbs}

    #return HttpResponse(s, content_type="text/plain; charset=utf-8")
    return HttpResponse(template.render(context, request))




