# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
from django.shortcuts import render,redirect
from django.core.urlresolvers import resolve
from .models import Investor,IndividualAddOn, OrganizationAddOn, Startup, StartupAddOn

# Create your views here.

def home(request):
   return render(request,'Homepage/index.html',)        #PENDING.........



#########################################
#               INVESTOR                #
#########################################
def genContext(request):
        investor = Investor.objects.get(id = int(request.session['id']))
        if(OrganizationAddOn.objects.filter(Username = investor).count() > 0):
                org = OrganizationAddOn.objects.get(Username = investor)
        else:
                org = None
                
        if(IndividualAddOn.objects.filter(Username = investor).count() > 0): 
                ind = IndividualAddOn.objects.get(Username = investor)
        else:
                ind = None
        context = {'investor':investor,'organization':org,'individual':ind}
        return context


def investor(request):  
    #login's code
    #If session exists render Investors Homepage     
    if("id" in request.session):

        context = genContext(request)
        return render(request,'Profile/profile_investor.html',context)   #!!SOLVED!! Issue must be Investor Home not detail form  

    #If Signup Button Pressed    
    if(request.method == "POST" and request.POST.get('Submit') == "Sign Up"):
        return Inv_Signup(request)
 
    #If Login Button Pressed    
    elif(request.method=="POST" and request.POST.get('Submit')=="Log In"):
        return Inv_Login(request)

    #No Forms Filled So GOTO Login Signup Page    
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
        return Inv_SetSession(request,investor)
        
              
        


def Inv_Login(request):
        print "In login"
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        
        #Logic For Login
        #if((Username == "Email" || Username == "Contact" || Username == "Email" )&& Password == "Password")
        login=False
        if("@" in username and "." in username):
                if(Investor.objects.filter(Email=username,Password=password)):
                        investor = Investor.objects.get(Email = username)
                        login=True
                        return Inv_SetSession(request,investor)   
                        
        if(str(username).isdigit()):
                if(Investor.objects.filter(Contact=username,Password=password)):
                        investor = Investor.objects.get(Contact = username)
                        login=True  
                        return Inv_SetSession(request,investor)
                        
                         
        else:
                if(Investor.objects.filter(Username=username,Password=password)):
                        investor = Investor.objects.get(Username = username)
                        login=True   
                        return Inv_SetSession(request,investor)
                        
        if login == False:
                context={
                        'existmsg':'Credentials Incorrect or Not Registered'
                }
                return render(request,'Homepage/investors_login_signup.html',context)     




def Inv_Organization(request):
        org = OrganizationAddOn() 
        ID = Investor.objects.get(id = int(request.session['id']))
        if OrganizationAddOn.objects.filter(Username = ID):
                org = OrganizationAddOn.objects.get(Username = ID)
        else:        
                org = OrganizationAddOn()
                org.Username = ID

        print request.POST.get('OrganizationType')  
        if not request.POST.get('OrganizationType')==None:
                org.OrganizationType=request.POST.get('OrganizationType')
        if not request.POST.get('URL')=="":
                org.URL=request.POST.get('URL')
        if not request.POST.get('YearFounded')=="":
                org.YearFounded=request.POST.get('YearFounded')
        if not request.POST.get('Size')=="":
                org.Size=request.POST.get('Size')
        if not request.POST.get('BusinessType')==None:
                org.BusinessType=request.POST.get('BusinessType')
        if not request.POST.get('Specialities')=="":
                org.Specialites=request.POST.get('Specialities')
        org.save()
        return redirect("/Investor/Edit/")
 

def Inv_Individual(request):
        ind = IndividualAddOn() 
        ID = Investor.objects.get(id = int(request.session['id']))
        if IndividualAddOn.objects.filter(Username = ID):
                ind = IndividualAddOn.objects.get(Username = ID)
        else:        
                ind = IndividualAddOn()
                ind.Username = ID
        
        ind.BusinessType = request.POST.get('BusinessType')
        ind.StartupsFunded = request.POST.get('StartupsFunded')
        ind.URL = request.POST.get('URL')
        ind.save()
        return redirect("/Investor/Edit/")


def Inv_SetSession(request,investor):
        request.session['id'] = investor.id        
        return redirect("/Investor/")



def inv_logout(request):
        for key in request.session.keys():
                del(request.session[key])
        return redirect("/Investor")
        

def inv_edit(request):
        
        ###################
        #     SECURITY    #
        ###################        
        #if session is not initialized the edit profile must not work
        if checksession(request):
                return redirect('/Investor')

        #Edit Profile Organization    
        if(request.method=="POST" and "Organization" in request.POST):
                return Inv_Organization(request)   

        #Edit Profile Individual    
        elif(request.method=="POST" and "Individual" in request.POST):
                return Inv_Individual(request)    
        
        elif(request.method == "POST" and request.POST.get('Submit') == "Upload"):
                #Handle File Upload
                ID = Investor.objects.get(id = int(request.session['id']))
                if IndividualAddOn.objects.filter(Username = ID):
                        ind = IndividualAddOn.objects.get(Username = ID)
                else:        
                        ind = IndividualAddOn()
                        ind.Username = ID
        
                ind.Pic = request.FILES['Pic'] 
                ind.save() 
                request.session['Pic'] = ind.Pic.url
                return redirect("/Investor/Edit") 
        context = genContext(request)
        context['edit'] = '1'
        return render(request,'Profile/edit.html',context)

def checksession(request):
         if("id" not in request.session):
                return True
        













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
                return render(request,'Profile/profile_startup.html')   #!!SOLVED!! Issue must be Investor Home not detail form  
                
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


        startup.Name=request.POST.get('Name')
        startup.Email=request.POST.get('Email')
        startup.Username=request.POST.get('Username')
        startup.Contact=request.POST.get('Contact')
        startup.City=request.POST.get('City')
        startup.Password=request.POST.get('Password')
        startup.save()
        Startup_SetSession(request,startup)



def startup_login(request):
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        
        #Logic For Login
        #if((Username == "Email" || Username == "Contact" || Username == "Email" )&& Password == "Password")

        login=False
        if("@" in username and "." in username):
                if(Startup.objects.filter(Email=username,Password=password)):
                        login=True
                        startup = Startup.objects.get(Email = username)
                        return Startup_SetSession(request,startup)   
                        

        if(str(username).isdigit()):
                if(Startup.objects.filter(Contact=username,Password=password)):
                        login=True  
                        startup = Startup.objects.get(Contact = username)
                        return Startup_SetSession(request,startup)
                        
                         
        else:
                if(Startup.objects.filter(Username=username,Password=password)):
                        login=True   
                        startup = Startup.objects.get(Username = username)
                        return Startup_SetSession(request,startup)
                        

        if login == False:
                context={
                        'existmsg':'Credentials Incorrect or Not Registered'
                }
                return render(request,'Homepage/startups_login_signup.html',context)    
        pass    


def Startup_SetSession(request,startup):
        request.session['Startup_id'] = startup.id
        request.session['Startup_Name'] = startup.Name 
        return redirect("/Startup/")


def Startup_addon(request):
        pass 




def Startup_logout(request):
        for key in request.session.keys():
                del(request.session[key])
        return redirect("/Startup")



#Chat bot REQUIRES pip install requests
def chatbot(request):
        quest = request.GET['question'];
        Answer = requests.get("botServerIp:PORT/?question=%s"% (quest))
        return  HttpResponse(Answer)
   