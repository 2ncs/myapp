#! /usr/bin/env python
# -*-coding: utf-8 -*-
#python 2
from unicodedata import normalize
from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *
from django.db.models import Q

# Create your views here.

def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form0 = search(request.POST)
        form1 = Search_bar(request.POST)
        form2 = Kouzines(request.POST)
        form3 = Street_Food(request.POST)
        form4 = Timh(request.POST)
        form5 = Loipa(request.POST)
        form6 = International(request.POST)
        form7 = lat_lon(request.POST)
        form8 = Aktina(request.POST)
        
        # check whether it's valid:
        if (form8.is_valid() and form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid() and form6.is_valid() and form7.is_valid() and form0.is_valid()) :
            onoma=form0.cleaned_data.get('onoma')
            if(onoma==""):    
                kouzina=0
                timh=0
                epiloges=0
                data_kouzina=[]
                data_timh=[]
                data_epiloges=[]
                a=[]
                perioxh=form1.cleaned_data.get('perioxh')
                lon=form7.cleaned_data.get('lon')
                lat=form7.cleaned_data.get('lat')
                aktina=form8.cleaned_data.get('aktina')
                data_aktina=[]
                locations=[]
                #res=form3.cleaned_data.get('souvlaki')
                
                if (form2.cleaned_data.get('bar_restaurant')==True):
                    kouzina=1
                    data=bar_rest()
                    for i in data:
                        data_kouzina.append(i.name.id)

                if (form2.cleaned_data.get('brunch')==True):
                    kouzina=1
                    data=brunch()
                    for i in data:
                        data_kouzina.append(i.name.id)

                if (form2.cleaned_data.get('mezedopoleia')==True):
                    kouzina=1
                    data=mezedopoleia()
                    for i in data:
                        data_kouzina.append(i.name.id)

                if (form2.cleaned_data.get('fusion')==True):
                    kouzina=1
                    data=fusion()
                    for i in data:
                        data_kouzina.append(i.name.id)

                if (form2.cleaned_data.get('ellhnikh_paradosiakh')==True):
                    kouzina=1
                    data=ellhnikh_paradosiakh()
                    for i in data:
                        data_kouzina.append(i.name.id)

                if (form6.cleaned_data.get('burger_amerikanikh')==True):
                    kouzina=1
                    data=burger_amerikanikh()
                    for i in data:
                        data_kouzina.append(i.name.id)

                if (form2.cleaned_data.get('vegeterian')==True):
                    kouzina=1
                    data=vegeterian()
                    for i in data:
                        data_kouzina.append(i.name.id)

                if (form2.cleaned_data.get('fish')==True):
                    kouzina=1
                    data=fish()
                    for i in data:
                        data_kouzina.append(i.name.id)

                if (form2.cleaned_data.get('mesogeiakh')==True):
                    kouzina=1
                    data=mesogeiakh()
                    for i in data:
                        data_kouzina.append(i.name.id)

                if (form2.cleaned_data.get('sigxronh_ellinikh')==True):
                    kouzina=1
                    data=sigxronh_ellhnikh()
                    for i in data:
                        data_kouzina.append(i.name.id)
                    
                if (form6.cleaned_data.get('indikh')==True):
                    kouzina=1
                    data=indikh()
                    for i in data:
                        data_kouzina.append(i.name.id)

                if (form6.cleaned_data.get('gallikh')==True):
                    kouzina=1
                    data=gallikh()
                    for i in data:
                        data_kouzina.append(i.name.id)

                if (form6.cleaned_data.get('italikh')==True):
                    kouzina=1
                    data=italikh()
                    for i in data:
                        data_kouzina.append(i.name.id)

                if (form2.cleaned_data.get('multi_ethnic')==True):
                    kouzina=1
                    data=multi_ethnic()
                    for i in data:
                        data_kouzina.append(i.name.id)

                if (form6.cleaned_data.get('afrikanikh')==True):
                    kouzina=1
                    data=afrikanikh()
                    for i in data:
                        data_kouzina.append(i.name.id)

                if (form6.cleaned_data.get('sushi')==True):
                    kouzina=1
                    data=sushi()
                    for i in data:
                        data_kouzina.append(i.name.id)

                if (form6.cleaned_data.get('ispanikh')==True):
                    kouzina=1
                    data=ispanikh()
                    for i in data:
                        data_kouzina.append(i.name.id)
                    
                if (form6.cleaned_data.get('latin')==True):
                    kouzina=1
                    data=latin()
                    for i in data:
                        data_kouzina.append(i.name.id)

                if (form2.cleaned_data.get('sigxronh')==True):
                    kouzina=1
                    data=sigxronh()
                    for i in data:
                        data_kouzina.append(i.name.id)
                    
                if (form6.cleaned_data.get('politikh')==True):
                    kouzina=1
                    data=politikh()
                    for i in data:
                        data_kouzina.append(i.name.id)

                if (form6.cleaned_data.get('asiatikh')==True):
                    kouzina=1
                    data=asiatikh()
                    for i in data:
                        data_kouzina.append(i.name.id)

                if (form2.cleaned_data.get('gliko')==True):
                    kouzina=1
                    data=glyko()
                    for i in data:
                        data_kouzina.append(i.name.id)
                    
                if (form2.cleaned_data.get('pagwto')==True):
                    kouzina=1
                    data=pagwto()
                    for i in data:
                        data_kouzina.append(i.name.id)

                if (form3.cleaned_data.get('souvlaki')==True):
                    kouzina=1
                    data=souvlaki()
                    for i in data:
                        data_kouzina.append(i.name.id)

                if (form3.cleaned_data.get('falafes')==True):
                    kouzina=1
                    data=falafes()
                    for i in data:
                        data_kouzina.append(i.name.id)
                    
                if (form3.cleaned_data.get('lagmatzoun')==True):
                    kouzina=1
                    data=lagmatzoun()
                    for i in data:
                        data_kouzina.append(i.name.id)

                if (form3.cleaned_data.get('sandwitch')==True):
                    kouzina=1
                    data=sandwitch()
                    for i in data:
                        data_kouzina.append(i.name.id)
                    
                if (form3.cleaned_data.get('krepa')==True):
                    kouzina=1
                    data=krepa()
                    for i in data:
                        data_kouzina.append(i.name.id)

                if (form3.cleaned_data.get('kotompoukies')==True):
                    kouzina=1
                    data=kotompoukies()
                    for i in data:
                        data_kouzina.append(i.name.id)

                if (form3.cleaned_data.get('mpougatsa_sfoliata')==True):
                    kouzina=1
                    data=mpougatsa()
                    for i in data:
                        data_kouzina.append(i.name.id)

                if (form3.cleaned_data.get('burger')==True):
                    kouzina=1
                    data=burger()
                    for i in data:
                        data_kouzina.append(i.name.id)

                #########################################################

                        
                if (form4.cleaned_data.get('deka')==True):
                    timh=1
                    data=Rests.objects.filter(price__exact='-10')
                    for i in data:
                        data_timh.append(i.id)

                if (form4.cleaned_data.get('deka_eikosi')==True):
                    timh=1
                    data=Rests.objects.filter(price__exact='10-20')
                    for i in data:
                        data_timh.append(i.id)

                if (form4.cleaned_data.get('eikosi_trianta')==True):
                    timh=1
                    data=Rests.objects.filter(price__exact='20-30')
                    for i in data:
                        data_timh.append(i.id)
                        
                if (form4.cleaned_data.get('trianta_saranta')==True):
                    timh=1
                    data=Rests.objects.filter(price__exact='30-40')
                    for i in data:
                        data_timh.append(i.id)    

                if (form4.cleaned_data.get('saranta_peninta')==True):
                    timh=1
                    data=Rests.objects.filter(price__exact='40-50')
                    for i in data:
                        data_timh.append(i.id)    

                if (form4.cleaned_data.get('peninta_kai')==True):
                    timh=1
                    data=Rests.objects.filter(price__exact='50-')
                    for i in data:
                        data_timh.append(i.id)
               ###############################################################

                if (form5.cleaned_data.get('live_music')==True):
                    epiloges=1
                    data=Rests.objects.filter(live_mousikh=True)
                    for i in data:
                        data_epiloges.append(i.id)


                if (form5.cleaned_data.get('for_kids')==True):
                    epiloges=1
                    data=Rests.objects.filter(for_kids=True)
                    for i in data:
                        data_epiloges.append(i.id)

                if (form5.cleaned_data.get('view')==True):
                    epiloges=1
                    data=Rests.objects.filter(view=True)
                    for i in data:
                        data_epiloges.append(i.id)


                if (form5.cleaned_data.get('romantic')==True):
                    epiloges=1
                    data=Rests.objects.filter(romantic=True)
                    for i in data:
                        data_epiloges.append(i.id)

                if (kouzina==0):
                    data=Rests.objects.all()
                    for i in data:
                        data_kouzina.append(i.id)

                if (timh==0):
                    data=Rests.objects.all()
                    for i in data:
                        data_timh.append(i.id)

                if (epiloges==0):
                    data=Rests.objects.all()
                    for i in data:
                        data_epiloges.append(i.id)

                data=Rests.objects.filter(Q(id__in=data_kouzina) & Q(id__in=data_timh) & Q(id__in=data_epiloges))

                if (aktina is None):
                    aktina=500
                
                if (perioxh):
                    for rest in data:
                        if (rest.distance(lon,lat)<=aktina):
                            data_aktina.append(rest.id)
                    data=Rests.objects.filter(Q(id__in=data_aktina))
                
                if (perioxh is None):
                    lat=37.9838096
                    lon=23.7275388

                for rest in data:
                    local=[rest.name.encode('utf_8'),rest.latitude,rest.longitude,1]
                    locations.append(local)
                ####################################    
                
                return render(request, 'search_engine/results.html', {'form8':form8,'form0':form0,'form1':form1, 'form2':form2, 'form3':form3,'form4':form4,'form5':form5,'form6':form6,'form7':form7,"detail":data,'stigma':locations,'lat':lat,'lon':lon})
            else:
                lat=0
                lon=0
                locations=[]
                data=Rests.objects.filter(name__contains=onoma)
                for rest in data:
                    lat=rest.latitude
                    lon=rest.longitude
                    local=[rest.name.encode('utf_8'),rest.latitude,rest.longitude,1]
                    locations.append(local)
                return render(request, 'search_engine/results.html', {'form8':form8,'form0':form0,'form1':form1, 'form2':form2, 'form3':form3,'form4':form4,'form5':form5,'form6':form6,'form7':form7,"detail":data,'stigma':locations,'lat':lat,'lon':lon})   
    # if a GET (or any other method) we'll create a blank form
    else:
        form1 = Search_bar()
        form2 = Kouzines()
        form3 = Street_Food()

    return render(request, 'search_engine/home.html', {'form8':Aktina,'form0':search,'form1': Search_bar,'form2': Kouzines, 'form3':Street_Food, 'form4':Timh, 'form5':Loipa,'form6':International,'form7':lat_lon})

################################################################################################################################
################################################################################################################################

def index_ins(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        #a=Rests.objects.get(pk=4)
        form1=ins(request.POST)
        form2=Kouzines(request.POST)
        form3=Street_Food(request.POST)
        if (form1.is_valid() and form2.is_valid() and form3.is_valid()):
            entry=form1.save()
            if (form2.cleaned_data.get('bar_restaurant')==True):
                a=Bar_Restaurant(name=entry)
                a.save()
                
            if (form2.cleaned_data.get('brunch')==True):
                a=Brunch(name=entry)
                a.save()
                
            if (form2.cleaned_data.get('mezedopoleia')==True):
                a=Mezedopoleia(name=entry)
                a.save()

            if (form2.cleaned_data.get('fusion')==True):
                a=Fusion(name=entry)
                a.save()

            if (form2.cleaned_data.get('ellhnikh_paradosiakh')==True):
                a=Ellhnikh_Paradosiakh(name=entry)
                a.save()

            if (form2.cleaned_data.get('burger_amerikanikh')==True):
                a=Burger_Amerikanikh(name=entry)
                a.save()

            if (form2.cleaned_data.get('vegeterian')==True):
                a=Vegeterian(name=entry)
                a.save()

            if (form2.cleaned_data.get('fish')==True):
                a=Fish(name=entry)
                a.save()

            if (form2.cleaned_data.get('mesogeiakh')==True):
                a=Mesogeiakh(name=entry)
                a.save()

            if (form2.cleaned_data.get('sigxronh_ellinikh')==True):
                a=Sigxronh_Ellhnikh(name=entry)
                a.save()
                
            if (form2.cleaned_data.get('indikh')==True):
                a=Indikh(name=entry)
                a.save()

            if (form2.cleaned_data.get('gallikh')==True):
                a=Gallikh(name=entry)
                a.save()

            if (form2.cleaned_data.get('italikh')==True):
                a=Italikh(name=entry)
                a.save()

            if (form2.cleaned_data.get('multi_ethnic')==True):
                a=Multi_Ethnic(name=entry)
                a.save()

            if (form2.cleaned_data.get('afrikanikh')==True):
                a=Afrikanikh(name=entry)
                a.save()

            if (form2.cleaned_data.get('sushi')==True):
                a=Sushi(name=entry)
                a.save()

            if (form2.cleaned_data.get('ispanikh')==True):
                a=Ispanikh(name=entry)
                a.save()
                
            if (form2.cleaned_data.get('latin')==True):
                a=Latin(name=entry)
                a.save()

            if (form2.cleaned_data.get('sigxronh')==True):
                a=Sigxronh(name=entry)
                a.save()
                
            if (form2.cleaned_data.get('politikh')==True):
                a=Politikh(name=entry)
                a.save()

            if (form2.cleaned_data.get('asiatikh')==True):
                a=Asiatikh(name=entry)
                a.save()

            if (form2.cleaned_data.get('gliko')==True):
                a=Glyko(name=entry)
                a.save()
                
            if (form2.cleaned_data.get('pagwto')==True):
                a=Pagwto(name=entry)
                a.save()

            if (form3.cleaned_data.get('souvlaki')==True):
                a=Souvlaki(name=entry)
                a.save()

            if (form3.cleaned_data.get('falafes')==True):
                a=Falafes(name=entry)
                a.save()
                
            if (form3.cleaned_data.get('lagmatzoun')==True):
                a=Lagmatzoun(name=entry)
                a.save()

            if (form3.cleaned_data.get('sandwitch')==True):
                a=Sandwitch(name=entry)
                a.save()
                
            if (form3.cleaned_data.get('krepa')==True):
                a=Krepa(name=entry)
                a.save()

            if (form3.cleaned_data.get('kotompoukies')==True):
                a=Kotompoukies(name=entry)
                a.save()

            if (form3.cleaned_data.get('mpougatsa_sfoliata')==True):
                a=Mpougatsa_Sfoliata(name=entry)
                a.save()

            if (form3.cleaned_data.get('burger')==True):
                a=Burger(name=entry)
                a.save()



            
            #if (form3.cleaned_data.get('souvlaki')==True):
                #kat=Souvlaki(name=entry)
                #kat.save()

            
            


            
        return render(request, 'search_engine/insert.html',{'form1':form1,'form2':form2,'form3':form3})
            
    else:
        form1=ins()
        form2=Kouzines()
        form3=Street_Food()
        return render(request, 'search_engine/insert.html',{'form1':form1,'form2':form2,'form3':form3})




def bar_rest():
    data=Bar_Restaurant.objects.all()
    return data

def brunch():
    data=Brunch.objects.all()
    return data

def mezedopoleia():
    data=Mezedopoleia.objects.all()
    return data

############StreetFood##########

def souvlaki():
    data=Souvlaki.objects.all()
    return data

def falafes():
    data=Falafes.objects.all()
    return data

def lagmatzoun():
    data=Lagmatzoun.objects.all()
    return data

def sandwitch():
    data=Sandwitch.objects.all()
    return data

def krepa():
    data=Krepa.objects.all()
    return data

def kotompoukies():
    data=Kotompoukies.objects.all()
    return data

def mpougatsa():
    data=Mpougatsa_Sfoliata.objects.all()
    return data

def burger():
    data=Burger.objects.all()
    return data

################################################################


def fusion():
    data=Fusion.objects.all()
    return data

def ellhnikh_paradosiakh():
    data=Ellhnikh_Paradosiakh.objects.all()
    return data

def burger_amerikanikh():
    data=Burger_Amerikanikh.objects.all()
    return data

def vegeterian():
    data=Vegeterian.objects.all()
    return data

def fish():
    data=Fish.objects.all()
    return data

def mesogeiakh():
    data=Mesogeiakh.objects.all()
    return data

def sigxronh_ellhnikh():
    data=Sigxronh_Ellhnikh.objects.all()
    return data


def indikh():
    data=Indikh.objects.all()
    return data

def gallikh():
    data=Gallikh.objects.all()
    return data

def italikh():
    data=Italikh.objects.all()
    return data

def multi_ethnic():
    data=Multi_Ethnic.objects.all()
    return data

def afrikanikh():
    data=Afrikanikh.objects.all()
    return data

def sushi():
    data=Sushi.objects.all()
    return data

def ispanikh():
    data=Ispanikh.objects.all()
    return data

def latin():
    data=Latin.objects.all()
    return data

def sigxronh():
    data=Sigxronh.objects.all()
    return data

def politikh():
    data=Politikh.objects.all()
    return data

def asiatikh():
    data=Asiatikh.objects.all()
    return data

def glyko():
    data=Glyko.objects.all()
    return data

def pagwto():
    data=Pagwto.objects.all()
    return data
















































    
