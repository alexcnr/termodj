# Generated by Django 3.1.7 on 2021-10-03 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('termoapp', '0003_t_sbp_dbp_s_br_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_sbp_dbp_s_br',
            name='temperature',
            field=models.FloatField(blank=True, null=True, verbose_name='Температура'),
        ),
    ]
