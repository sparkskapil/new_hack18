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


class ProblemSolution(models.Model):
    Problem = models.CharField(max_length=200)
    Need = models.CharField(max_length=200)
    ExistingSolution = models.CharField(max_length=200)
    How = models.CharField(max_length=200)
    AddressedNeeds = models.CharField(max_length=200)
    Better = models.CharField(max_length=200)

#   AddOn FINAL PORTFOLIO   #
#############################
class StartupAddOn(models.Model):
    Status = models.CharField(max_length=50)
    Stage = models.CharField(max_length=100)
    Tagline = models.CharField(max_length=100)
    Website = models.CharField(max_length=100)
    BusinessSector = models.CharField(max_length=100)
    Problem = models.ForeignKey('ProblemSolution')
    UVP = models.CharField(max_length=1000)
    CompetitiveAdvantage = models.CharField(max_length=1000)
    TargetCustomers = models.CharField(max_length=500)
    Threats = models.CharField(max_length=200)
    Summary = models.CharField(max_length=1000)
    LOGO =  Image = models.ImageField(upload_to="Team",blank = True)
    # MarketValidation


class FeasibilityScore(models.Model):
    StartupId = models.ForeignKey('Startup')
    Score = models.PositiveSmallIntegerField(default=1, blank=True, null=True)

class Product(models.Model):
    Name = models.CharField(max_length=100)
    ProductImage = models.ImageField(upload_to="Team",default="Team/default.jpg")
    startup = models.ForeignKey('Startup')

class Associate(models.Model):
    Name = models.CharField(max_length=100)
    Designation = models.CharField(max_length=100)
    Responsibility = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Image = models.ImageField(upload_to="Team",default="Team/default.jpg")
    startup = models.ForeignKey('Startup')

class Competitor(models.Model):
    Name = models.CharField(max_length=100)
    Strength = models.CharField(max_length=1000)
    Weakness = models.CharField(max_length=1000)
    startup = models.ForeignKey('Startup')









class PortFolio(models.Model):
    InvestorId = models.ForeignKey('Investor')
    StartupId  = models.ForeignKey('Startup')
    InvRequest = models.CharField(max_length=100, default="PENDING")
    StrRequest = models.CharField(max_length=100, default="PENDING")
    InvPortfolio = models.BooleanField(default=False)
    StrPortfolio = models.BooleanField(default=False)

class Filters(models.Model):
    InvestorId = models.ForeignKey('Investor')
    FilterName = models.CharField(max_length=100, default="")
    Loction = models.CharField(max_length=100, default="")
    BSector = models.CharField(max_length=100, default="")
    StartupStage = models.CharField(max_length=100, default="")