from django.contrib import admin

# Register your models here.
from .models import Bb, T_SBP_DBP_S_BR
from .models import Rubric # для объявлений

#класс редактор, он хорош для моделей с несколькими  значащими полями
class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric' )
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')

#класс редактор, он хорош для моделей с несколькими  значащими полями
class T_SBP_DBP_S_BRAdmin(admin.ModelAdmin):
    list_display = ('title', 'sex', 'temperature', 'saturation', 'published' )
    list_display_links = ('title', 'sex')
    search_fields = ('title', 'sex')



admin.site.register(Bb, BbAdmin)
admin.site.register(T_SBP_DBP_S_BR, T_SBP_DBP_S_BRAdmin)
admin.site.register(Rubric)



