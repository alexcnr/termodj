from django.urls import path
from . import views




urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.index),
]

# Здесь index это имя функции из views