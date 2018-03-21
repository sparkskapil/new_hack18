# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import Investor
# Create your views here.

def home(request):
   return render(request,'Homepage/index.html',)

def investor(request):
    if(request.method == "POST"):
        investor = Investor()
        
        if(Investor.objects.filter(Email=request.POST.get('Username'))):
                context={
                        'existmsg':'User already exists'
                }
                return render(request,'Homepage/investor_present.html',context)
        
        investor.Email = request.POST.get('Username')
        investor.Name = request.POST.get('Name')
        investor.Password = request.POST.get('Password')
        investor.save()
        
        a=request.POST.get('Username')
        context={
                'greet':a
        }
        return render(request,'Homepage/investorDetails.html',context)
    else:   
        return render(request,'Homepage/Investor.html',)


    
