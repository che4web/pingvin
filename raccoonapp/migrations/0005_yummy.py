# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-12 03:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('raccoonapp', '0004_auto_20190301_0447'),
    ]

    operations = [
        migrations.CreateModel(
            name='Yummy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('raccoon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raccoonapp.Raccoon')),
            ],
        ),
    ]
