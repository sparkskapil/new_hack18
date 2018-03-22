# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Investor(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Username = models.CharField(max_length=100,default="")
    Contact = models.CharField(max_length=15,default="123456")
    City = models.CharField(max_length=20,default="Pune")
    Password = models.CharField(max_length=100)
	

class IndividualAddOn(models.Model):
    Username = models.ForeignKey('Investor')
    BusinessType=models.CharField(max_length=50)
    StartupsFunded=models.CharField(max_length=5)
    URL=models.CharField(max_length=50)
    

class OrganizationAddOn(models.Model):
    Username=models.ForeignKey('Investor')
    OrganizationType=models.CharField(max_length=50)
    URL=models.CharField(max_length=50)
    YearFounded=models.CharField(max_length=4)
    Size=models.CharField(max_length=6)
    BusinessType=models.CharField(max_length=50)
    Specialites = models.CharField(max_length=500)



##########################################################################
        #STARTUPS 
##########################################################################
#   SIGNUP DETAILS  #
#####################
class Startup(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Username = models.CharField(max_length=100,default="")
    Contact = models.CharField(max_length=15,default="123456")
    City = models.CharField(max_length=20,default="Pune")
    Password = models.CharField(max_length=100)

#   AddOn FINAL PORTFOLIO   #
#############################
class StartupAddOn(models.Model):
    


        








