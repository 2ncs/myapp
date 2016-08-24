from unicodedata import normalize
from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *
from django.db.models import Q

# Create your views here.
def index(request):
    if request.method == 'POST':
            form1=search(request.POST)
            form2=Search_bar(request.POST)
            form3=Aktina(request.POST)
            form4=lat_lon(request.POST)
            form5=Kind_of_bar(request.POST)
            form6=Tags(request.POST)
            if (form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid() and form6.is_valid()):
                onoma=form1.cleaned_data.get('onoma')
                if (onoma==""):
                    bars=0
                    tags=0
                    data_bar=[]
                    data_tags=[]
                    perioxh=form2.cleaned_data.get('perioxh')
                    lon=form4.cleaned_data.get('lon')
                    lat=form4.cleaned_data.get('lat')
                    aktina=form3.cleaned_data.get('aktina')
                    data_aktina=[]
                    locations=[]
                    ################
                    if(form5.cleaned_data.get('club')==True):
                            bars=1
                            data=club()
                            for i in data:
                                data_bar.append(i.name.id)


                    if(form5.cleaned_data.get('bar')==True):
                            bars=1
                            data=bar()
                            for i in data:
                                data_bar.append(i.name.id)


                    if(form5.cleaned_data.get('cafe')==True):
                            bars=1
                            data=cafe()
                            for i in data:
                                data_bar.append(i.name.id)

                                
                    if(form5.cleaned_data.get('cocktail_bar')==True):
                            bars=1
                            data=cocktail_bar()
                            for i in data:
                                data_bar.append(i.name.id)


                    if(form5.cleaned_data.get('wine_bar')==True):
                            bars=1
                            data=wine_bar()
                            for i in data:
                                data_bar.append(i.name.id)

                                
                    if(form5.cleaned_data.get('beer_pub')==True):
                            bars=1
                            data=wine_bar()
                            for i in data:
                                data_bar.append(i.name.id)

                    ###############################################

                    if(form6.cleaned_data.get('roof')==True):
                            tags=1
                            data=Cafe_Bar.objects.filter(roof=True)
                            for i in data:
                                data_tags.append(i.id)


                    if(form6.cleaned_data.get('garden')==True):
                            tags=1
                            data=Cafe_Bar.objects.filter(garden=True)
                            for i in data:
                                data_tags.append(i.id)



                    if(form6.cleaned_data.get('romantic')==True):
                            tags=1
                            data=Cafe_Bar.objects.filter(romantic=True)
                            for i in data:
                                data_tags.append(i.id)


                    if(form6.cleaned_data.get('view')==True):
                            tags=1
                            data=Cafe_Bar.objects.filter(view=True)
                            for i in data:
                                data_tags.append(i.id)


                    if(form6.cleaned_data.get('gay_lesbian')==True):
                            tags=1
                            data=Cafe_Bar.objects.filter(gay_lesbian=True)
                            for i in data:
                                data_tags.append(i.id)



                    if(form6.cleaned_data.get('dance')==True):
                            tags=1
                            data=Cafe_Bar.objects.filter(dance=True)
                            for i in data:
                                data_tags.append(i.id)


                    if(form6.cleaned_data.get('rock')==True):
                            tags=1
                            data=Cafe_Bar.objects.filter(rock=True)
                            for i in data:
                                data_tags.append(i.id)


                    if(form6.cleaned_data.get('techno')==True):
                            tags=1
                            data=Cafe_Bar.objects.filter(techno=True)
                            for i in data:
                                data_tags.append(i.id)


                    if(form6.cleaned_data.get('rempetiko_ellhniko')==True):
                            tags=1
                            data=Cafe_Bar.objects.filter(rempetiko_ellhniko=True)
                            for i in data:
                                data_tags.append(i.id)


                    if(form6.cleaned_data.get('jazz')==True):
                            tags=1
                            data=Cafe_Bar.objects.filter(jazz=True)
                            for i in data:
                                data_tags.append(i.id)


                    if(form6.cleaned_data.get('chill')==True):
                            tags=1
                            data=Cafe_Bar.objects.filter(chill=True)
                            for i in data:
                                data_tags.append(i.id)


                    if(form6.cleaned_data.get('whiskes')==True):
                            tags=1
                            data=Cafe_Bar.objects.filter(whiskes=True)
                            for i in data:
                                data_tags.append(i.id)



                    if(form6.cleaned_data.get('mpouzoukia')==True):
                            tags=1
                            data=Cafe_Bar.objects.filter(mpouzoukia=True)
                            for i in data:
                                data_tags.append(i.id)


                    if(form6.cleaned_data.get('live_music')==True):
                            tags=1
                            data=Cafe_Bar.objects.filter(live_music=True)
                            for i in data:
                                data_tags.append(i.id)


                    if(form6.cleaned_data.get('beach_bar')==True):
                            tags=1
                            data=Cafe_Bar.objects.filter(beach_bar=True)
                            for i in data:
                                data_tags.append(i.id)

                    ###############################

                    if (bars==0):
                            data=Cafe_Bar.objects.all()
                            for i in data:
                                data_bar.append(i.id)        



                    if (tags==0):
                        data=Cafe_Bar.objects.all()
                        for i in data:
                            data_tags.append(i.id)


                    data=Cafe_Bar.objects.filter(Q(id__in=data_bar) & Q(id__in=data_tags))


                    if (aktina is None):
                            aktina=1


                    if (perioxh):
                            for shp in data:
                                if (shp.distance(lon,lat)<=aktina):
                                    data_aktina.append(shp.id)
                            data=Cafe_Bar.objects.filter(Q(id__in=data_aktina))


                    if (perioxh is None):
                            lat=37.9838096
                            lon=23.7275388


                    for shp in data:
                            local=[shp.name.encode('utf_8'),shp.latitude,shp.longitude,1]
                            locations.append(local)



                    return render(request,"cafe_bars/results.html",{'form1':form1,'form2':form2,'form3':form3,'form4':form4,'form5':form5,'form6':form6,"detail":data,'stigma':locations,'lat':lat,'lon':lon})


                else:
                        lat=0
                        lon=0
                        locations=[]
                        data=Shop.objects.filter(name__contains=onoma)
                        for shp in data:
                            lat=shp.latitude
                            lon=shp.longitude
                            local=[shp.name.encode('utf_8'),shp.latitude,shp.longitude,1]
                            locations.append(local)
                        return render(request,"cafe_bars/results.html",{'form1':form1,'form2':form2,'form3':form3,'form4':form4,'form5':form5,'form6':form6,"detail":data,'stigma':locations,'lat':lat,'lon':lon})     
        

    return render(request,"cafe_bars/cafe_bars_home.html",{'form1':search(),'form2':Search_bar(),'form3':Aktina(),'form4':lat_lon(),'form5':Kind_of_bar(),'form6':Tags()})





def club():
        data=Club.objects.all()
        return data


def bar():
        data=Bar.objects.all()
        return data

def cafe():
        data=cafe.objects.all()
        return data


def cocktail_bar():
        data=Cocktail_bar.objects.all()
        return data    

def wine_bar():
        data=Wine_bar.objects.all()
        return data


def beer_pub():
        data=Beer_pub.objects.all()
        return data    
    

                                

