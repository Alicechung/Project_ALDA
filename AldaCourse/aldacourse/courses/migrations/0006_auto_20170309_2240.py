# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 22:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_remove_testchoice_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chooseins',
            name='courseins',
        ),
        migrations.RemoveField(
            model_name='chooseins',
            name='id',
        ),
        migrations.AddField(
            model_name='chooseins',
            name='inspk',
            field=models.CharField(default='', max_length=30, primary_key=True, serialize=False),
        ),
    ]
