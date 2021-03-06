# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-31 08:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0006_activefilter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='associate',
            name='startup',
        ),
        migrations.RemoveField(
            model_name='competitor',
            name='startup',
        ),
        migrations.RemoveField(
            model_name='feasibilityscore',
            name='StartupId',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='InvestorId',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='StartupId',
        ),
        migrations.RemoveField(
            model_name='problemsolution',
            name='startup',
        ),
        migrations.RemoveField(
            model_name='product',
            name='startup',
        ),
        migrations.RemoveField(
            model_name='startupaddon',
            name='startup',
        ),
        migrations.DeleteModel(
            name='Associate',
        ),
        migrations.DeleteModel(
            name='Competitor',
        ),
        migrations.DeleteModel(
            name='FeasibilityScore',
        ),
        migrations.DeleteModel(
            name='PortFolio',
        ),
        migrations.DeleteModel(
            name='ProblemSolution',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='StartupAddOn',
        ),
    ]
