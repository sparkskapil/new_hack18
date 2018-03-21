# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Investor(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
	

class IndividualAddOn(models.Model):
    Username = ""
    BusinessType=models.CharField(max_length=50)
    StartupsFunded=models.CharField(max_length=5)
    URL=models.CharField(max_length=50)
    

class OrganizationAddOn(models.Model):
    Username=""
    OrganizationType=models.CharField(max_length=50)
    URL=models.CharField(max_length=50)
    YearFounded=models.CharField(max_length=4)
    Size=models.CharField(max_length=6)
    BusinessType=models.CharField(max_length=50)
    Specialites = models.CharField(max_length=500)










