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
    BusinessType=models.CharField(max_length=50,blank=True)
    StartupsFunded=models.CharField(max_length=5,blank=True)
    URL=models.CharField(max_length=50,blank=True)
    Pic=models.ImageField(upload_to="profile",blank=True)
    

class OrganizationAddOn(models.Model):
    Username=models.ForeignKey('Investor')
    OrganizationType=models.CharField(max_length=50)
    URL=models.CharField(max_length=50)
    YearFounded=models.CharField(max_length=4)
    Size=models.CharField(max_length=6)
    BusinessType=models.CharField(max_length=50)
    Specialites = models.CharField(max_length=500)

class Filter(models.Model):
    Username = models.ForeignKey('Investor')
    Name = models.CharField(max_length=50)
    BusinessSector = models.CharField(max_length=50,null=True)
    Location = models.CharField(max_length=50,null=True)
    Stage = models.CharField(max_length=50,null=True)

class ActiveFilter(models.Model):
    Username = models.ForeignKey('Investor')
    ActiveFilter = models.ForeignKey('Filter')
##########################################################################
        #STARTUPS 
##########################################################################
#   SIGNUP DETAILS  #
#####################
class Startup(models.Model):
    Name = models.CharField(max_length=100)     #Startup Name
    Email = models.CharField(max_length=100)
    Username = models.CharField(max_length=100,default="")
    Contact = models.CharField(max_length=15,default="123456")
    City = models.CharField(max_length=20,default="Pune")
    Password = models.CharField(max_length=100)


class StartupAddOn(models.Model):
    Status = models.CharField(max_length=100,null = True) 
    Stage = models.CharField(max_length=100,null = True) 
    Logo = models.ImageField(upload_to="Startup",blank=True)
    Website = models.CharField(max_length=100,null = True) 
    Tagline = models.CharField(max_length=100,null = True) 
    StartupSector = models.CharField(max_length=100,null = True) 
    ProductName = models.CharField(max_length=100,null = True) 
    ProductImage = models.ImageField(upload_to="Startup",blank=True)
    startup = models.ForeignKey('Startup')

class Customers(models.Model):
    Customer = models.CharField(max_length=100,null = True) 
    Metric = models.CharField(max_length=100,null = True)
    startup = models.ForeignKey('Startup')

class Problem(models.Model):
    Problem = models.CharField(max_length=100,null = True) 
    ProblemImg = models.ImageField(upload_to="Startup",blank=True)
    startup = models.ForeignKey('Startup')

class Solution(models.Model):
    Solution = models.CharField(max_length=100,null = True) 
    SolutionImg = models.ImageField(upload_to="Startup",blank=True)
    startup = models.ForeignKey('Startup')

class Team(models.Model):
    Name=models.CharField(max_length=100,null = True) 
    Designation = models.CharField(max_length=100,null = True) 
    Responsiblity = models.CharField(max_length=100,null = True) 
    Email = models.CharField(max_length=100,null = True) 
    startup = models.ForeignKey('Startup')

class Competitor(models.Model):
    Name = models.CharField(max_length=100,null = True) 
    Image = models.ImageField(upload_to="Startup",blank=True)
    Opportunity = models.CharField(max_length=100,null = True) 
    startup = models.ForeignKey('Startup')

class Funding(models.Model):    
    Name = models.CharField(max_length=100,null = True) 
    Metric = models.CharField(max_length=100,null = True) 
    startup = models.ForeignKey('Startup')

class Sales(models.Model):
    Year = models.CharField(max_length=100,null = True) 
    Sales = models.CharField(max_length=100,null = True) 
    Expenses = models.CharField(max_length=100,null = True) 
    startup = models.ForeignKey('Startup')

class BusinessModel(models.Model):    
    Parameter = models.CharField(max_length=100,null = True) 
    Metric = models.CharField(max_length=100,null = True) 
    startup = models.ForeignKey('Startup')

class MarketValidation(models.Model):    
    Parameter = models.CharField(max_length=100,null = True) 
    Metric = models.CharField(max_length=100,null = True) 
    startup = models.ForeignKey('Startup')
