# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import Investor, OrganizationAddOn
# Create your views here.

def home(request):
   return render(request,'Homepage/index.html',)

def investor(request):
    if(request.method == "POST" and request.POST.get('Submit') == "Signup"):
        Signup(request)
        #login's code
    elif(request.method=="POST" and request.POST.get('Submit')=="Login"):
        Login(request)
        
        #ORhanization's code
    elif(request.method=="POST" and request.POST.get('Submit')==""):
        Login(request)   

    elif(request.method=="POST" and request.POST.get('Submit')=="Login"):
        Login(request)    

    else:   
        return render(request,'Homepage/Investor.html',)


    
def Signup(request):
        investor = Investor()
        if(Investor.objects.filter(Email=request.POST.get('Email'))):
                context={
                        'existmsg':'User already exists'
                }
                return render(request,'Homepage/investor_present.html',context)
        investor.Name = request.POST.get('Name')  
        investor.Contact = request.POST.get('Contact')    
        investor.Email = request.POST.get('Email')
        investor.City = request.POST.get('City')
        investor.Username = request.POST.get('Username')
        investor.Password = request.POST.get('Password')
        investor.save()
        a=investor.Name
        context={
                'greet':a
        }
        return render(request,'Homepage/investorDetails.html',context)


def Login(request):
        pass


def Organization(request):
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
 




def Individual(request):
        pass


