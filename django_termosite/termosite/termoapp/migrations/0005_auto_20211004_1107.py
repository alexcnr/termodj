# Generated by Django 3.1.7 on 2021-10-04 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('termoapp', '0004_auto_20211003_1318'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='Название рубрики')),
            ],
            options={
                'verbose_name': 'Название рубрики',
                'verbose_name_plural': 'Названия рубрик',
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='bb',
            options={'ordering': ['-published'], 'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AlterModelOptions(
            name='t_sbp_dbp_s_br',
            options={'ordering': ['-published'], 'verbose_name': 'Пациент', 'verbose_name_plural': 'Пациенты'},
        ),
        migrations.AlterField(
            model_name='bb',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='bb',
            name='published',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='t_sbp_dbp_s_br',
            name='published',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано'),
        ),
        migrations.AddField(
            model_name='bb',
            name='rubric',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='termoapp.rubric', verbose_name='Название рубрики'),
        ),
    ]
