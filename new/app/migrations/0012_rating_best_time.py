# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-19 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_place_hotel'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='best_time',
            field=models.CharField(choices=[('morning', 'MORNING'), ('day', 'Day'), ('evening', 'Evening'), ('night', 'Night')], default='day', max_length=4),
        ),
    ]