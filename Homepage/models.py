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


class ProblemSolution(models.Model):
    What = models.CharField(max_length=200)
    Need = models.CharField(max_length=200)
    ExistSolution = models.CharField(max_length=200)

    How = models.CharField(max_length=200)
    Satisfies = models.CharField(max_length=200)
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
    UVP = models.CharField(max_length=200)
    CompetitiveAdvantage = models.CharField(max_length=200)
    TargetCustomers = models.CharField(max_length=200)
    Threats = models.CharField(max_length=200)
    Summary = models.CharField(max_length=1000)
    #LOGO
    # MarketValidation
    # Team 
    #Competitors = models.CharField(max_length=1000)
    
class FeasibilityScore(models.Model):
    StartupId = models.ForeignKey('Startup')
    Score = models.PositiveSmallIntegerField(default=1, blank=True, null=True)

class PortFolio(models.Model):
    InvestorId = models.ForeignKey('Investor')
    StartupId  = models.ForeignKey('Startup')
    InvRequest = models.CharField(max_length=100, default="PENDING")
    StrRequest = models.CharField(max_length=100, default="PENDING")
    InvPortfolio = models.BooleanField(default=False)
    StrPortfolio = models.BooleanField(default=False)