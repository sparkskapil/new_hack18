# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

from .models import Investor,IndividualAddOn, OrganizationAddOn, Startup, StartupAddOn

# Create your views here.

def home(request):
   return render(request,'Homepage/index.html',)        #PENDING

def investor(request):  
    #If session exists render Investors Homepage    
    if(request.method == "POST" and request.POST.get('Submit') == "Upload"):
        #Handle File Upload
        ID = Investor.objects.get(id = int(request.session['id']))
        
        if IndividualAddOn.objects.filter(id = request.session['id']):
                ind = IndividualAddOn.objects.get(Username = ID)
        else:        
                ind = IndividualAddOn()
                ind.Username = ID
        
        ind.Pic = request.FILES['Pic'] 
        ind.save() 
        
        request.session['Pic'] = ind.Pic.url
        
        return redirect("/Investor/") 
      
    #login's code
 
    if("id" in request.session):
        return render(request,'Homepage/InvestorProfile.html')   #!!SOLVED!! Issue must be Investor Home not detail form  
        
    if(request.method == "POST" and request.POST.get('Submit') == "Sign Up"):
        return Inv_Signup(request)

    elif(request.method=="POST" and request.POST.get('Submit')=="Log In"):
        return Inv_Login(request)
        
        #Organization's code
    elif(request.method=="POST" and "Organization" in request.POST):
        return Inv_Organization(request)   

    elif(request.method=="POST" and "Individual" in request.POST):
        return Inv_Individual(request)    

    else:   
        return render(request,'Homepage/investors_login_signup.html',)


    
def Inv_Signup(request):
        investor = Investor()
        #UNIQUE EMAIL CHECK
        if(Investor.objects.filter(Email=request.POST.get('Email'))):
                context={
                        'existmsg':'Email already exists'
                }
                return render(request,'Homepage/investors_login_signup.html',context)
        
        #UNIQUE MOBILE NUMBER CHECK        
        if(Investor.objects.filter(Contact=request.POST.get('Contact'))):
                context={
                        'existmsg':'Contact already exists'
                }
                return render(request,'Homepage/investors_login_signup.html',context)

        #UNIQUE USERNAME CHECK               
        if(Investor.objects.filter(Username=request.POST.get('Username'))):
                context={
                        'existmsg':'Username already exists'
                }
                return render(request,'Homepage/investors_login_signup.html',context) 
        investor.Name = request.POST.get('Name')  
        investor.Contact = request.POST.get('Contact')    
        investor.Email = request.POST.get('Email')
        investor.City = request.POST.get('City')
        investor.Username = request.POST.get('Username')
        investor.Password = request.POST.get('Password')
        investor.save()

        request.session['id'] = investor.id
        request.session['Name'] = investor.Name
              
        return render(request,'Homepage/InvestorProfile.html')#!!SOLVED!! Issue must be Investor Home not detail form 



def Inv_Login(request):
        print "In login"
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        
        #Logic For Login
        #if((Username == "Email" || Username == "Contact" || Username == "Email" )&& Password == "Password")
        login=False
        if("@" in username and "." in username):
                if(Investor.objects.filter(Email=username,Password=password)):
                        SetSession(request)   
                        login=True

        if(str(username).isdigit()):
                if(Investor.objects.filter(Contact=username,Password=password)):
                        SetSession(request)
                        login=True  
                         
        else:
                if(Investor.objects.filter(Username=username,Password=password)):
                        SetSession(request)
                        login=True   

        if login == False:
                context={
                        'existmsg':'Credentials Incorrect or Not Registered'
                }
                return render(request,'Homepage/investors_login_signup.html',context)     


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

def startup(request):
        if(request.method == "POST" and request.POST.get('Submit') == "Upload"):
        #Handle File Upload
                ID = Startup.objects.get(id = int(request.session['Startup_id']))
                
                if StartupAddOn.objects.filter(id = request.session['Startup_id']):
                        std = StartupAddOn.objects.get(Username = ID)
                else:        
                        std = StartupAddOn()
                        std.Username = ID
                
                ind.Pic = request.FILES['Pic'] 
                ind.save() 
                
                request.session['Pic'] = ind.Pic.url
                
                return redirect("/Startup/") 
      
        #login's code
 
        if("Startup_id" in request.session):
                return render(request,'Homepage/StartupProfile.html')   #!!SOLVED!! Issue must be Investor Home not detail form  
                
        if(request.method == "POST" and request.POST.get('Submit') == "Sign Up"):
                return startup_signup(request)

        elif(request.method=="POST" and request.POST.get('Submit')=="Log In"):
                return startup_login(request)
                
  

        else:   
                return  render(request,'Homepage/startups_login_signup.html')



def startup_signup(request):
        
        if(Startup.objects.filter(Email=request.POST.get('Email'))):
                context={
                        'existmsg':'Email already exists'
                }
                return render(request,'Homepage/startups_login_signup.html',context)
                
        
        #UNIQUE MOBILE NUMBER CHECK        
        if(Startup.objects.filter(Contact=request.POST.get('Contact'))):
                context={
                        'existmsg':'Contact already exists'
                }
                
                return render(request,'Homepage/startups_login_signup.html',context)

        #UNIQUE USERNAME CHECK               
        if(Startup.objects.filter(Username=request.POST.get('Username'))):
                context={
                        'existmsg':'Username already exists'
                }
                
                return render(request,'Homepage/investors_login_signup.html',context) 
        
        startup=Startup()


        startup.Name=request.POST.get()
        startup.Email=request.POST.get()
        startup.Username=request.POST.get()
        startup.Contact=request.POST.get()
        startup.City=request.POST.get()
        startup.Password=request.POST.get()
        startup.save()

        return render(request,'Homepage/startups_login_signup.html')

        pass


def startup_login(request):
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        
        #Logic For Login
        #if((Username == "Email" || Username == "Contact" || Username == "Email" )&& Password == "Password")
        login=False
        if("@" in username and "." in username):
                if(Startup.objects.filter(Email=username,Password=password)):
                       Startup_SetSession(request)   
                        login=True

        if(str(username).isdigit()):
                if(Startup.objects.filter(Contact=username,Password=password)):
                        Startup_SetSession(request)
                        login=True  
                         
        else:
                if(Startup.objects.filter(Username=username,Password=password)):
                        Startup_SetSession(request)
                        login=True   

        if login == False:
                context={
                        'existmsg':'Credentials Incorrect or Not Registered'
                }
                return render(request,'Homepage/startups_login_signup.html',context)    
        pass    


def Startup_SetSession(request):
        request.session['Startup_id'] = startup.id
        request.session['Startup_Name'] = startup.Name 
        redirect("/startup/")


def Startup_addon(request):
        pass 