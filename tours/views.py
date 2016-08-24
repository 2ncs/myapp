#! /usr/bin/env python
# -*-coding: utf-8 -*-
#python 2
from unicodedata import normalize
from django.shortcuts import render
from django.http import *
from .forms import *
from .models import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
# Create your views here.


class photo(ListView):
        model=image
        context_object_name="data"
        template_name='tours/photos.html'
        
        def get_queryset(self):
                return image.objects.filter(name__id=self.kwargs['q'])



def index(request):
   if request.user.is_authenticated():
      form1=search()
      form2=radio(initial={'choice':'ALL'})
      return render(request,"tours/tours.html",{'form1':form1,'form2':form2})
   else:
      return HttpResponseRedirect('/login/')
  

def thematic(request):
        if request.user.is_authenticated():
           form1=search()
           form2=radio(initial={'choice':'ALL'})
           return render(request,"tours/thematic.html",{'form1':form1,'form2':form2})
        else:
                return HttpResponseRedirect('/login/')


def Classic(request):
        if request.user.is_authenticated():
              data=classic.objects.all()
              return render(request,"tours/results.html",{'data':data})
        else:
                return HttpResponseRedirect('/login/')
        

def Classic_private(request):
        if request.user.is_authenticated():
              data=classic.objects.filter(name__private_group__exact='PRIVATE')
              return render(request,"tours/results.html",{'data':data})
        else:
                return HttpResponseRedirect('/login/')        
        




def Classic_group(request):
        if request.user.is_authenticated():
              data=classic.objects.filter(name__private_group__exact='GROUP')
              return render(request,"tours/results.html",{'data':data})
        else:
                return HttpResponseRedirect('/login/')
        
        
   

def Bus(request):
        if request.user.is_authenticated():
              data=bus.objects.all()
              return render(request,"tours/results.html",{'data':data})
        else:
                return HttpResponseRedirect('/login/')


def Bus_private(request):
        if request.user.is_authenticated():
              data=bus.objects.filter(name__private_group__exact='PRIVATE')
              return render(request,"tours/results.html",{'data':data})
        else:
                return HttpResponseRedirect('/login/')


def Bus_group(request):
        if request.user.is_authenticated():
                data=bus.objects.filter(name__private_group__exact='GROUP')
                return render(request,"tours/results.html",{'data':data})
        else:
                return HttpResponseRedirect('/login/')
        



def Cruises(request):
        if request.user.is_authenticated():
              data=cruises.objects.all()
              return render(request,"tours/results.html",{'data':data})
        else:
                return HttpResponseRedirect('/login/')


def Cruises_private(request):
        if request.user.is_authenticated():
              data=cruises.objects.filter(name__private_group__exact='PRIVATE')
              return render(request,"tours/results.html",{'data':data})
        else:
                return HttpResponseRedirect('/login/')


def Cruises_group(request):
        if request.user.is_authenticated(): 
              data=cruises.objects.filter(name__private_group__exact='GROUP')
              return render(request,"tours/results.html",{'data':data})
        else:
                return HttpResponseRedirect('/login/')


def Bicycle(request):
        if request.user.is_authenticated(): 
              data=bicycle.objects.all()
              return render(request,"tours/results.html",{'data':data})
        else:
                return HttpResponseRedirect('/login/')


def Bicycle_private(request):
        if request.user.is_authenticated():
              data=bicycle.objects.filter(name__private_group__exact='PRIVATE')
              return render(request,"tours/results.html",{'data':data})
        else:
                return HttpResponseRedirect('/login/')
        


def Bicycle_group(request):
        if request.user.is_authenticated():
              data=bicycle.objects.filter(name__private_group__exact='GROUP')
              return render(request,"tours/results.html",{'data':data})
        else:
                return HttpResponseRedirect('/login/')
   

def Excursions(request):
        if request.user.is_authenticated():
              data=excursions.objects.all()
              return render(request,"tours/results.html",{'data':data})
        else:
                return HttpResponseRedirect('/login/')


def Excursions_private(request):
        if request.user.is_authenticated():
              data=excursions.objects.filter(name__private_group__exact='PRIVATE')
              return render(request,"tours/results.html",{'data':data})
        else:
                return HttpResponseRedirect('/login/')
        


def Excursions_group(request):
        if request.user.is_authenticated():
              data=excursions.objects.filter(name__private_group__exact='GROUP')
              return render(request,"tours/results.html",{'data':data})
        else:
                return HttpResponseRedirect('/login/')


def Thematic_Kids_And_Family(request):
        if request.user.is_authenticated():
              data=thematic_kids_and_family.objects.all()
              return render(request,"tours/results.html",{'data':data})
        else:
                return HttpResponseRedirect('/login/')


def Thematic_Kids_And_Family_private(request):
        if request.user.is_authenticated():
              data=thematic_kids_and_family.objects.filter(name__private_group__exact='PRIVATE')
              return render(request,"tours/results.html",{'data':data})
        else:
                return HttpResponseRedirect('/login/')
   

def Thematic_Kids_And_Family_group(request):
        if request.user.is_authenticated():
                data=thematic_kids_and_family.objects.filter(name__private_group__exact='GROUP')
                return render(request,"tours/results.html",{'data':data})
        else:
                return HttpResponseRedirect('/login/')


def Thematic_Gastronomy(request):
        if request.user.is_authenticated():
              data=thematic_gastronomy.objects.all()
              return render(request,"tours/results.html",{'data':data})
        else:
                return HttpResponseRedirect('/login/')


def Thematic_Gastronomy_private(request):
        if request.user.is_authenticated():
              data=thematic_gastronomy.objects.filter(name__private_group__exact='PRIVATE')
              return render(request,"tours/results.html",{'data':data})
        else:
                return HttpResponseRedirect('/login/')


def Thematic_Gastronomy_group(request):
        if request.user.is_authenticated():
              data=thematic_gastronomy.objects.filter(name__private_group__exact='GROUP')
              return render(request,"tours/results.html",{'data':data})
        else:
                return HttpResponseRedirect('/login/')


def Thematic_Photo(request):
        if request.user.is_authenticated():
              data=thematic_photo.objects.all()
              return render(request,"tours/results.html",{'data':data})
        else:
                return HttpResponseRedirect('/login/')


def Thematic_Photo_private(request):
        if request.user.is_authenticated():
              data=thematic_photo.objects.filter(name__private_group__exact='PRIVATE')
              return render(request,"tours/results.html",{'data':data})
        else:
                return HttpResponseRedirect('/login/')
        

def Thematic_Photo_group(request):
        if request.user.is_authenticated():
              data=thematic_photo.objects.filter(name__private_group__exact='GROUP')
              return render(request,"tours/results.html",{'data':data})
        else:
                return HttpResponseRedirect('/login/')



def Thematic_Street_Art(request):
        if request.user.is_authenticated():
              data=thematic_street_art.objects.all()
              return render(request,"tours/results.html",{'data':data})
        else:
                return HttpResponseRedirect('/login/')


def Thematic_Street_Art_private(request):
        if request.user.is_authenticated():
              data=thematic_street_art.objects.filter(name__private_group__exact='PRIVATE')
              return render(request,"tours/results.html",{'data':data})
        else:
                return HttpResponseRedirect('/login/')


def Thematic_Street_Art_group(request):
      data=thematic_street_art.objects.filter(name__private_group__exact='GROUP')
      return render(request,"tours/results.html",{'data':data})


def Thematic_Political(request):
        if request.user.is_authenticated():
              data=thematic_political.objects.all()
              return render(request,"tours/results.html",{'data':data})
        else:
                return HttpResponseRedirect('/login/')


def Thematic_Political_private(request):
        if request.user.is_authenticated():
              data=thematic_political.objects.filter(name__private_group__exact='PRIVATE')
              return render(request,"tours/results.html",{'data':data})
        else:
                return HttpResponseRedirect('/login/')


def Thematic_Political_group(request):
        if request.user.is_authenticated():
              data=thematic_political.objects.filter(name__private_group__exact='GROUP')
              return render(request,"tours/results.html",{'data':data})
        else:
                return HttpResponseRedirect('/login/')


def Thematic_Segway(request):
        if request.user.is_authenticated():
              data=thematic_segway.objects.all()
              return render(request,"tours/results.html",{'data':data})
        else:
                return HttpResponseRedirect('/login/')


def Thematic_Segway_private(request):
        if request.user.is_authenticated():
              data=thematic_segway.objects.filter(name__private_group__exact='PRIVATE')
              return render(request,"tours/results.html",{'data':data})
        else:
                return HttpResponseRedirect('/login/')


def Thematic_Segway_group(request):
        if request.user.is_authenticated():
              data=thematic_segway.objects.filter(name__private_group__exact='GROUP')
              return render(request,"tours/results.html",{'data':data})
        else:
                return HttpResponseRedirect('/login/')

@login_required(login_url="login/")
def search_result(request):
   if(request.method=='GET'):
      form1=search()
      form2=radio(initial={'choice':'ALL'})
      return render(request,"tours/tours.html",{'form1':form1,'form2':form2})

   
   else:
      form1 = search(request.POST)
      form2=radio(request.POST)
      if(form1.is_valid() and form2.is_valid()):
         onoma=form1.cleaned_data.get('onoma')
         choice=form2.cleaned_data.get('choice')
         if(choice=="GROUP"):
            data=Tour.objects.filter(Q(name__contains=onoma) | Q(perigrafh__contains=onoma) | Q(timetable__contains=onoma) | Q(diarkeia__contains=onoma) | Q(kostos__contains=onoma) | Q(category__contains=onoma) | Q(private_group__exact="GROUP"))
         if(choice=="PRIVATE"):
            data=Tour.objects.filter(Q(name__contains=onoma) | Q(perigrafh__contains=onoma) | Q(timetable__contains=onoma) | Q(diarkeia__contains=onoma) | Q(kostos__contains=onoma) | Q(category__contains=onoma) | Q(private_group__exact="PRIVATE"))
         else:
            data=Tour.objects.filter(Q(name__contains=onoma) | Q(perigrafh__contains=onoma) | Q(timetable__contains=onoma) | Q(diarkeia__contains=onoma) | Q(kostos__contains=onoma) | Q(category__contains=onoma))
            
   return render(request,"tours/results_Tour.html",{'data':data})
   
