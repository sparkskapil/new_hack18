# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

from .models import Investor,IndividualAddOn, OrganizationAddOn

# Create your views here.

def home(request):
   return render(request,'Homepage/index.html',)

def investor(request):
    #If session exists render Investors Homepage    
    if("id" in request.session):
        render(request,'Homepage/investorDetails.html',context)   #Issue must be Investor Home not detail form  

    if(request.method == "POST" and request.POST.get('Submit') == "Signup"):
        Signup(request)
        #login's code
    elif(request.method=="POST" and request.POST.get('Submit')=="Login"):
        Login(request)
        
        #ORhanization's code
    elif(request.method=="POST" and "Organization" in request.POST):
        Organization(request)   

    elif(request.method=="POST" and "Individual" in request.POST):
        Individual(request)    

    else:   
        return render(request,'Homepage/Investor.html',)


    
def Inv_Signup(request):
        investor = Investor()
        #UNIQUE EMAIL CHECK
        if(Investor.objects.filter(Email=request.POST.get('Email'))):
                context={
                        'existmsg':'Email already exists'
                }
                return render(request,'Homepage/investor_present.html',context)
        
        #UNIQUE MOBILE NUMBER CHECK        
        if(Investor.objects.filter(Contact=request.POST.get('Contact'))):
                context={
                        'existmsg':'Contact already exists'
                }
                return render(request,'Homepage/investor_present.html',context)

        #UNIQUE USERNAME CHECK               
        if(Investor.objects.filter(Username=request.POST.get('Username'))):
                context={
                        'existmsg':'Username already exists'
                }
                return render(request,'Homepage/investor_present.html',context) #Issue must be Investor Home not detail form 

        investor.Name = request.POST.get('Name')  
        investor.Contact = request.POST.get('Contact')    
        investor.Email = request.POST.get('Email')
        investor.City = request.POST.get('City')
        investor.Username = request.POST.get('Username')
        investor.Password = request.POST.get('Password')
        investor.save()

        request.session['id'] = investor.id
        request.session['Name'] = investor.Name
        
        a=investor.Name
        context={
                'greet':a
        }
        return render(request,'Homepage/investorDetails.html',context)


def Inv_Login(request):
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        
        #Logic For Login
        #if((Username == "Email" || Username == "Contact" || Username == "Email" )&& Password == "Password")
        
        if("@" in Username and "." in Username):
                if(Investor.objects.filter(Email=username,Password=password)):
                        SetSession(request)   

        if(Username.isDigit()):
                if(Investor.objects.filter(Contact=username,Password=password)):
                        SetSession(request)  
                         
        else:
                if(Investor.objects.filter(Username=username,Password=password)):
                        SetSession(request)   
                


def Inv_Organization(request):
        org= OrganizationAddOn() 
        id=request.session['id']

        org.Username=id
        org.OrganizationType=request.POST.get('')
        org.URL=request.POST.get('Website')
        org.YearFounded=request.POST.get('Year founded')
        org.Size=request.POST.get('size')
        org.BussinessType=request.POST.get('Company Type')
        org.Specialties=request.POST.get('Specialties')
        org.save()
        return render(request,'Homepage/investorDetails.html')
 




def Inv_Individual(request):
        id = request.session['id']
        ind = IndividualAddOn()
        ind.Username = id
        ind.BusinessType = request.POST.get('BusinessType')
        ind.StartupsFunded = request.POST.get('StartupsFunded')
        ind.URL = request.POST.get('URL')
        ind.save()


def Inv_SetSession(request):
        request.session['id'] = investor.id
        request.session['Name'] = investor.Name 
        redirect("/Investor/")





##########################################################################
        #STARTUPS
##########################################################################


