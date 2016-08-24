if request.method == 'POST':
        form1=search(request.POST)
        form2=Search_bar(request.POST)
        form3=Aktina(request.POST)
        form4=lat_lon(request.POST)
        form5=Kind_of_shop(request.POST)
        form6=Tags(request.POST)
        if (form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid() and form6.is_valid()):
            onoma=form1.cleaned_data.get('onoma')
            if (onoma==""):
                shop=0
                tags=0
                data_shop=[]
                data_tag=[]
                perioxh=form2.cleaned_data.get('perioxh')
                lon=form4.cleaned_data.get('lon')
                lat=form4.cleaned_data.get('lat')
                aktina=form3.cleaned_data.get('aktina')
                data_aktina=[]
                locations=[]
                ############
                if(form5.cleaned_data.get('souvenir')==True):
                    shop=1
                    data=souvenir()
                    for i in data:
                        data_shop.append(i.name.id)


                if(form5.cleaned_data.get('delicatessen')==True):
                    shop=1
                    data=delicatessen()
                    for i in data:
                        data_shop.append(i.name.id)


                if(form5.cleaned_data.get('kosmhma')==True):
                    shop=1
                    data=kosmhma()
                    for i in data:
                        data_shop.append(i.name.id)

                        
                if(form5.cleaned_data.get('moda')==True):
                    shop=1
                    data=moda()
                    for i in data:
                        data_shop.append(i.name.id)


                if(form6.cleaned_data.get('greek_design')==True):
                    tags=1
                    data=Shop.objects.filter(greek_design=True)
                    for i in data:
                        data_tags.append(i.id)


                if(form6.cleaned_data.get('handmade')==True):
                    tags=1
                    data=Shop.objects.filter(handmade=True)
                    for i in data:
                        data_tags.append(i.id)


                if(form6.cleaned_data.get('not_expensive')==True):
                    tags=1
                    data=Shop.objects.filter(not_expensive=True)
                    for i in data:
                        data_tags.append(i.id)
                        

                if(form6.cleaned_data.get('gift')==True):
                    tags=1
                    data=Shop.objects.filter(gift=True)
                    for i in data:
                        data_tags.append(i.id)



                if(form6.cleaned_data.get('kids')==True):
                    tags=1
                    data=Shop.objects.filter(kids=True)
                    for i in data:
                        data_tags.append(i.id)
                        


                if(form6.cleaned_data.get('traditional')==True):
                    tags=1
                    data=Shop.objects.filter(traditional=True)
                    for i in data:
                        data_tags.append(i.id)



                if(form6.cleaned_data.get('men')==True):
                    tags=1
                    data=Shop.objects.filter(men=True)
                    for i in data:
                        data_tags.append(i.id)


                if(form6.cleaned_data.get('women')==True):
                    tags=1
                    data=Shop.objects.filter(women=True)
                    for i in data:
                        data_tags.append(i.id)



                if(form6.cleaned_data.get('ceramics')==True):
                    tags=1
                    data=Shop.objects.filter(ceramics=True)
                    for i in data:
                        data_tags.append(i.id)



                if (shop==0):
                    data=Shop.objects.all()
                    for i in data:
                        data_shop.append(i.id)        



                if (tags==0):
                    data=Shop.objects.all()
                    for i in data:
                        data_tags.append(i.id)        


                data=Shop.objects.filter(Q(id__in=data_shop) & Q(id__in=data_tags))



                if (aktina is None):
                    aktina=1


                if (perioxh):
                        for shp in data:
                            if (shp.distance(lon,lat)<=aktina):
                                data_aktina.append(rest.id)
                        data=Shop.objects.filter(Q(id__in=data_aktina))


                if (perioxh is None):
                    lat=37.9838096
                    lon=23.7275388


                for shp in data:
                    local=[shp.name.encode('utf_8'),shp.latitude,shp.longitude,1]
                    locations.append(local)    

                ####################################################    
                return render(request,"shopping/shopping_home.html")


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
                return render(request,"shopping/shopping_home.html")
