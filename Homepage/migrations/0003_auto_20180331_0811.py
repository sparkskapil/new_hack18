# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-31 02:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0002_filter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filters',
            name='InvestorId',
        ),
        migrations.DeleteModel(
            name='Filters',
        ),
    ]
