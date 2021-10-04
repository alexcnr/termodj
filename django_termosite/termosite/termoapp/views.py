#from django import template
#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.template import loader

from .models import Bb, T_SBP_DBP_S_BR

from django.shortcuts import render
 
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



    #template = loader.get_template('termoapp/index.html')   ЭТО БОЛЕЕ ПОНЯТНЫЙ ВАРИАНТ
    
    
    
    #bbs = Bb.objects.order_by('-published')  #  это В 1 ВАРИАНТЕ
    #pps = T_SBP_DBP_S_BR.objects.order_by('-published')  #  это В 1 ВАРИАНТЕ

    bbs = Bb.objects.all()  #  это В 2 ВАРИАНТЕ, когда мы уже отсортировали в модели в классе Мета
    pps = T_SBP_DBP_S_BR.objects.all()  #  это В 2 ВАРИАНТЕ  когда мы уже отсортировали в модели в классе Мета




        ## передаем словарь переменных для рендеринга, в книге пока этого не было  ###
         # ЭТО БОЛЕЕ ПОНЯТНЫЙ ВАРИАНТ
    #context = {'bbs': bbs, 
    #           'pps': pps
    #}
    #return HttpResponse(template.render(context, request))        #БОЛЕЕ ПОНЯТНЫЙ ВАРИАНТ

    return render(request, 'termoapp/index.html', {'bbs': bbs, 
               'pps': pps
    }
    )







