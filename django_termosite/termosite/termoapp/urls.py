from django.urls import path
from . import views
from . views import index, by_rubric




urlpatterns = [
    #path('', views.index, name='index'),
    
    #path('', views.index),
    path('<int:rubric_id>/', by_rubric),
    path('', index),
]

# Здесь index это имя функции из views