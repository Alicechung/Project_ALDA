# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 22:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_testchoice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testchoice',
            name='id',
        ),
        migrations.AddField(
            model_name='testchoice',
            name='testpk',
            field=models.CharField(default='', max_length=30, primary_key=True, serialize=False),
        ),
    ]
