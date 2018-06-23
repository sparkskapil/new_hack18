# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
from django.shortcuts import render,redirect
from django.core.urlresolvers import resolve
from .models import *#Investor,IndividualAddOn, OrganizationAddOn, Startup, StartupAddOn, Filter

# Create your views here.

def home(request):
   return render(request,'Homepage/index.html',)       

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
        if(Filter.objects.filter(Username = investor).count() > 0):
                filters = Filter.objects.filter(Username = investor)
        else:    
                filters = None
        context = {'investor':investor,'organization':org,'individual':ind,'filters':filters}
        if(ActiveFilter.objects.filter(Username = investor).count() > 0):
                accfilter = ActiveFilter.objects.get(Username = investor)
        else:    
                accfilter = None
          
        context = {'investor':investor,'organization':org,'individual':ind,'filters':filters,'ActiveFilter':accfilter}
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
                return redirect("/Investor/Edit") 
        context = genContext(request)
        context['edit'] = '1'
        return render(request,'Profile/edit.html',context)

def checksession(request):
         if("id" not in request.session):
                return True
        




def filter(request):
       
        ID = Investor.objects.get(id = int(request.session['id']))
        if (request.method=="POST" and request.POST.get("Submit")=="Add"):
                
                if Filter.objects.filter(Username = ID, Name = request.POST.get("Name")):
                        filter = Filter.objects.get(Username = ID, Name = request.POST.get("Name"))
                else:
                        filter = Filter()
                filter.Name = request.POST.get("Name")
                filter.BusinessSector = request.POST.get("BusinessSector")
                filter.Location = request.POST.get("Location")
                filter.Stage = request.POST.get("Stage")
                filter.Username = ID
                filter.save()
                return redirect("/Investor/Filter")
                
        elif (request.method=="POST" and request.POST.get("Submit")=="Delete"):
                filter = Filter.objects.get(id = int(request.POST.get("id")))
                filter.delete()
                return redirect("/Investor/Filter")
                
        context = genContext(request)
        context['filter'] = '1'
        if Filter.objects.filter(Username = ID):
                context['filter_count'] = Filter.objects.filter(Username = ID).count()
        return render(request,"Profile/addfilter.html",context)
        pass



def ActivateFilter(request):
        filter_id = request.GET['id']
        ID = Investor.objects.get(id = int(request.session['id']))

        if(filter_id == "All"):
                if ActiveFilter.objects.filter(Username = ID):
                        accfilter = ActiveFilter.objects.get(Username = ID)
                        accfilter.delete()
                redirect("/Investor/")  

        else:
                Filt = Filter.objects.get(id=filter_id)
                if ActiveFilter.objects.filter(Username = ID):
                        accfilter = ActiveFilter.objects.get(Username = ID)
                else:
                        accfilter = ActiveFilter()   

                accfilter.Username = ID
                accfilter.ActiveFilter = Filt
                accfilter.save()
                return redirect("/Investor/")
        return redirect("/Investor/")






##########################################################################
        #STARTUPS
##########################################################################




def Startup_Edit(request):
        if(request.method=='POST'):
                startup = Startup.objects.get(id = int(request.session['Startup_id']))
                if StartupAddOn.objects.filter(startup = startup):
                        AddOn = StartupAddOn.objects.get(startup = startup)
                else:
                        AddOn = StartupAddOn()

                if(not request.POST.get('startup_status') == ""):
                        AddOn.Status = request.POST.get('startup_status')
                if(not request.POST.get('startup_stage') == ""):
                        AddOn.Stage = request.POST.get('startup_stage')
               
               #IMAGE
                if 'logo_img' in  request.FILES.keys() :
                        AddOn.Logo = request.FILES['logo_img']
                
                if(not request.POST.get('tagline') == ""):
                        AddOn.Tagline = request.POST.get('tagline')
                if(not request.POST.get('startup_website') == ""):
                        AddOn.Website = request.POST.get('startup_website')
                if(not request.POST.get('startup_sector') == ""):
                        AddOn.StartupSector = request.POST.get('startup_sector')
                
                if(not request.POST.get("product_name") == ""):
                        AddOn.ProductName = request.POST.get('product_name')
                
                if 'product_image' in  request.FILES.keys() :
                        AddOn.ProductImage = request.FILES['product_image']

                '''

                Customers1 = request.POST.getlist("Customer[]")
                metrics =  request.POST.getlist("customer_metric[]")

                if not max(len(Customers1),len(metrics)) == 0:
                        if(Customers.objects.filter(startup = startup)>0):
                                customers= Customers.objects.filter(startup = startup)
                                for customer in customers:
                                        customer.delete()

                            
                for i in range(0,max(len(Customers1),len(metrics))):
                        C = Customers()
                        if i<len(Customers1):
                                C.Customer = Customers1[i]
                        if(i<len(metrics):
                                C.Metric = metrics[i]
                        C.startup = startup
                        C.save()
                
              
                 
                Problems = request.POST.getlist("Problem[]")
                problemimgs = request.FILES.getlist("problemimg[]")
            
                if not max(len(Problems),len(problemimgs)) == 0:
                        if(Problem.objects.filter(startup = startup)>0):
                                problems = Problem.objects.filter(startup = startup)
                                for problem in problems:
                                        problem.delete()
                
                for j in range(0,max(len(problems),len(problemimgs))):
                       
                        P = Problem()
                        if(j<len(Problems)):
                                P.Problem = Problems[j]
                        if(j<len(problemimgs)):
                                P.ProblemImg = problemimgs[j]
                        P.startup = startup
                        P.save()

                
                Solutions = request.POST.getlist("Solution[]")
                slutionimgs = request.POST.getlist("problemimg[]")
                
                if not max(len(Solutions),len(solutionimgs)) == 0:
                        if(Solution.objects.filter(startup = startup)>0):
                                solutions = Solution.objects.filter(startup = startup)
                                for solution in solutions:
                                        solution.delete()
               
                for i in range(0,max(len(solutions),len(solutionimgs))):
                        C = Solution()
                        if i < len(Solutions):
                                C.Solution = solution[i]
                        if i < len(solutionimgs):
                                C.SolutionImg = solutionimg[i]
                        C.startup = startup
                        C.save()
                
                
                Teams = request.POST.getlist("member_name[]")
                Designations =  request.POST.getlist("designation[]")
                Responsibilities =  request.POST.getlist("responsibilities[]")
                Emails =  request.POST.getlist("email[]")
                teamimgs = request.POST.getlist("teamimg[]")
                
                if not len(Teams) == 0:
                        if(Team.objects.filter(startup = startup)>0):
                                teams = Team.objects.filter(startup = startup)
                                for team in teams:
                                        team.delete()
                
                for i in range(0,len(Teams)):
                        C = Team()
                        if i < len(Teams):
                                C.Name = Teams[i]
                        if i < len(Designations):
                                C.Designation = Designations[i]
                        if i < len(Responsibilities):
                                C.Responsibility = Responsibilities[i]
                        if i < len(Emails):
                                C.Email = Emails[i]
                        C.startup = startup
                        C.save()
                
                Competetors = request.POST.getlist("Competitor[]")
                Opportunities =  request.POST.getlist("Opportunity[]")
                compimg =  request.POST.getlist("competitorimg[]")
                
                if(not len(Competetors) == 0):
                        if(Competitor.objects.filter(startup = startup)>0):
                                competitors = Competitor.objects.filter(startup = startup)
                                for competitor in competitors:
                                        competitor.delete()
                
                for i in range(0,len(Competetors)):
                        C = Compet  
                
                if(Funding.objects.filter(startup = startup)>0):
                        fundings = Funding.objects.filter(startup = startup)
                        for funding in fundings:
                                funding.delete()

                if(Sales.objects.filter(startup = startup)>0):
                        sales = Sales.objects.filter(startup = startup)
                        for sale in sales:
                                sale.delete()

                if(BusinessModel.objects.filter(startup = startup)>0):
                        businessmodels = BusinessModel.objects.filter(startup = startup)
                        for businessmodel in businessmodels:
                                businessmodel.delete()

                if(MarketValidation.objects.filter(startup = startup)>0):
                        marketvalidations = marketvalidation.objects.filter(startup = startup)
                        for marketvalidation in marketvalidations:
                                marketvalidation.delete() 
                '''
                
                        
                AddOn.startup = startup
                AddOn.save()

        context = genContextStartup(request)
        context['edit'] = '1'
        return render(request,"Profile/edit_startup.html",context)


def genContextStartup(request):
        startup = Startup.objects.get(id = int(request.session['Startup_id']))
        # if(OrganizationAddOn.objects.filter(Username = investor).count() > 0):
        #         org = OrganizationAddOn.objects.get(Username = investor)
        # else:
        #         org = None
                
        if(StartupAddOn.objects.filter(startup = startup).count() > 0): 
                addon = StartupAddOn.objects.get(startup = startup)
        else:
                addon = None

        context = {'startup':startup,'addon':addon}
        return context



def startup(request):
        if(request.method == "POST" and request.POST.get('Submit') == "Upload"):
        #Handle File Upload
                ID = Startup.objects.get(id = int(request.session['Startup_id']))
                
                if StartupAddOn.objects.filter(id = request.session['Startup_id']):
                        std = StartupAddOn.objects.get(startup = ID)
                else:        
                        std = StartupAddOn()
                        std.startup = ID
                
                ind.Pic = request.FILES['Pic'] 
                ind.save() 
                
                request.session['Pic'] = ind.Pic.url
                
                return redirect("/Startup/") 
      
        #login's code
 
        if("Startup_id" in request.session):
                context = genContextStartup(request)
               
                return render(request,'Profile/profile_startup.html',context)   #!!SOLVED!! Issue must be Investor Home not detail form  
                
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
        return Startup_SetSession(request,startup)
         


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
   