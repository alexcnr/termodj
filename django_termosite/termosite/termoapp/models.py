# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
# Unable to inspect table 'Results'
# The error was: cannot unpack non-iterable NoneType object

class Bb(models.Model):
    #rubric = models.ForeignKey(SubRubric, on_delete=models.PROTECT,
    #                                      verbose_name='Рубрика')
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    #contacts = models.TextField(verbose_name='Контакты')
    #image = models.ImageField(blank=True, upload_to=get_timestamp_path,
    #                          verbose_name='Изображение')
    #author = models.ForeignKey(AdvUser, on_delete=models.CASCADE,
    #                           verbose_name='Автор объявления')
    published = models.DateTimeField(auto_now_add=True, db_index=True)


class T_SBP_DBP_S_BR(models.Model):
    #rubric = models.ForeignKey(SubRubric, on_delete=models.PROTECT,
    #                                      verbose_name='Рубрика')
    title = models.CharField(max_length=50, verbose_name='ФИО')
    sex = models.TextField(max_length=10, blank=True, verbose_name='Пол')
    temperature = models.FloatField(null=True, blank=True, verbose_name='Температура')
    sbp = models.IntegerField(null=True, blank=True, verbose_name='САД')
    dbp = models.IntegerField(null=True, blank=True, verbose_name='ДАД')
    saturation = models.IntegerField(null=True, blank=True, verbose_name='Сатурация')
    breath_rate = models.IntegerField(null=True, blank=True, verbose_name='Сатурация')
    #contacts = models.TextField(verbose_name='Контакты')
    #image = models.ImageField(blank=True, upload_to=get_timestamp_path,
    #                          verbose_name='Изображение')
    #author = models.ForeignKey(AdvUser, on_delete=models.CASCADE,
    #                           verbose_name='Автор объявления')
    published = models.DateTimeField(auto_now_add=True, db_index=True)