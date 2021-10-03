"""termosite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#####   здесь  пишутся маршруты уровня проекта        #####

from django.contrib import admin
from django.urls import path
from django.urls import include
from termoapp import views
#from . import views

urlpatterns = [
    #path('termoapp/', include('termoapp.urls')),
    path('termoapp/', views.index),
    
    path('admin/', admin.site.urls),
    
    
]
###   urlpatterns - список маршрутов      ## 

# Используйте include() чтобы добавлять URL из каталога приложения

#urlpatterns += [
#     path('termoapp/', include('termoapp.urls')),
#]

# Добавьте URL соотношения, чтобы перенаправить запросы с корневого URL, на URL приложения


# Используйте static() чтобы добавить соотношения для статических файлов
# Только на период разработки
#from django.conf import settings
#from django.conf.urls.static import static

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

