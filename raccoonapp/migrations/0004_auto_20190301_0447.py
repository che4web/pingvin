# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-01 04:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('raccoonapp', '0003_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'verbose_name': 'Фотография енота', 'verbose_name_plural': 'Фотографии енотов'},
        ),
        migrations.AlterModelOptions(
            name='raccoon',
            options={'permissions': (('can_be', 'can be'),), 'verbose_name': 'Енот', 'verbose_name_plural': 'Еноты'},
        ),
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='raccoon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raccoonapp.Raccoon', verbose_name='Енот'),
        ),
        migrations.AlterField(
            model_name='raccoon',
            name='age',
            field=models.IntegerField(verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='raccoon',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='raccoon',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='raccoon',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='raccoonapp.Raccoon', verbose_name='Родитель'),
        ),
    ]
