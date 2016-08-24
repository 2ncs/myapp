# -*- coding: utf-8 -*-

from django import forms
from .models import *

class search(forms.Form):
        onoma = forms.CharField(label='Αναζήτηση Μαγαζιού', max_length=100,required=False,widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))



class Search_bar(forms.Form):
        perioxh = forms.CharField(label='Περιοχή', max_length=100,required=False,widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
        


class Aktina(forms.Form):
        aktina = forms.FloatField(label='Ακτίνα',required=False,widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))



class lat_lon(forms.Form):        
        lat = forms.FloatField(label='latitude',required=False)
        lon = forms.FloatField(label='longitude',required=False)

class Kouzines(forms.Form):
        bar_restaurant = forms.BooleanField(label='Bar Restaurant',required=False)
        brunch = forms.BooleanField(label='Brunch',required=False)
        mezedopoleia = forms.BooleanField(label='Μεζεδοπολεία',required=False)
        fusion = forms.BooleanField(label='Fusion',required=False)
        ellhnikh_paradosiakh = forms.BooleanField(label='Ελληνική Παραδοσιακή',required=False)
        vegeterian = forms.BooleanField(label='Vegeterian',required=False)
        fish = forms.BooleanField(label='Ψάρι',required=False)
        mesogeiakh = forms.BooleanField(label='Μεσογειακή',required=False)
        sigxronh_ellinikh = forms.BooleanField(label='Σύγχρονη Ελληνική',required=False)
        multi_ethnic = forms.BooleanField(label='Multi Ethnic',required=False)
        sigxronh = forms.BooleanField(label='Σύγχρονη',required=False)
        gliko = forms.BooleanField(label='Γλυκό',required=False)
        pagwto = forms.BooleanField(label='Παγωτό',required=False)
        international = forms.BooleanField(label='Διεθνείς',required=False)
        street_food = forms.BooleanField(label='Street Food',required=False)


class International(forms.Form):
        burger_amerikanikh = forms.BooleanField(label='Burger-Αμερικάνικη',required=False)
        ispanikh = forms.BooleanField(label='Ισπανική',required=False)
        italikh = forms.BooleanField(label='Ιταλική',required=False)
        sushi = forms.BooleanField(label='Sushi',required=False)
        afrikanikh = forms.BooleanField(label='Αφρικάνικη',required=False)
        politikh = forms.BooleanField(label='Πολίτικη',required=False)
        indikh = forms.BooleanField(label='Ινδική',required=False)
        gallikh = forms.BooleanField(label='Γαλλική',required=False)
        latin = forms.BooleanField(label='Λάτιν',required=False)
        asiatikh = forms.BooleanField(label='Ασιατική',required=False)



class Street_Food(forms.Form):
        souvlaki = forms.BooleanField(label='Σουβλάκι',required=False)
        falafes = forms.BooleanField(label='Φαλάφελ',required=False)
        lagmatzoun = forms.BooleanField(label='Λαγματζούν',required=False)
        sandwitch = forms.BooleanField(label='Σάντουϊτς',required=False)
        krepa = forms.BooleanField(label='Κρέπα',required=False)
        kotompoukies = forms.BooleanField(label='Κοτομπουκιές',required=False)
        mpougatsa_sfoliata = forms.BooleanField(label='Μπουγάτσα-Σφολιάτα',required=False)
        burger = forms.BooleanField(label='Burger',required=False)
        

class Loipa(forms.Form):
        live_music=forms.BooleanField(label='Ζωντανή Μουσική',required=False)
        for_kids=forms.BooleanField(label='Κατάλληλο Για Παιδιά',required=False)
        view=forms.BooleanField(label='Όμορφο Τοπίο',required=False)
        romantic=forms.BooleanField(label='Ρομαντικό',required=False)
        #xwris_filtro=forms.BooleanField(label='Χωρίς Φίλτρο',required=False)

class Timh(forms.Form):
        deka=forms.BooleanField(label='Έως 10 ευρώ',required=False)
        deka_eikosi=forms.BooleanField(label='10-20',required=False)
        eikosi_trianta=forms.BooleanField(label='20-30',required=False)
        trianta_saranta=forms.BooleanField(label='30-40',required=False)
        saranta_peninta=forms.BooleanField(label='40-50',required=False)
        peninta_kai=forms.BooleanField(label='50 και πάνω',required=False)
        #lefta_yparxoun=forms.BooleanField(label='Χωρίς Φίλτρο',required=False)

class Onoma(forms.Form):
       onoma = forms.CharField(label='Όνομα', max_length=100,required=True)

class Perioxh(forms.Form):
        perioxh = forms.CharField(label='Περιοχή', max_length=100,required=False)

class Dieuthinsh(forms.Form):
        dieuthinsh=forms.CharField(label='Διεύθυνση', max_length=100,required=True)


class Perifereia(forms.Form):
        perifereia=forms.CharField(label='Περιφέρεια', max_length=100,required=False)


class ins(forms.ModelForm):
        class Meta:
            model = Rests
            fields=['id','dieuthinsh','longitude','latitude','name','perioxh','periferia','price','live_mousikh','for_kids','view','romantic','cozy','site','e_table','thl','rate','butlair_link','stigma','comments']
        




class NameForm(forms.Form):
    
        your_name = forms.CharField(label='Search', max_length=100)
        what_for = forms.BooleanField(label='Souvlaki',required=False)


class NameForm2(forms.Form):
    
        your_name = forms.CharField(label='Your name', max_length=100)
        what_for = forms.BooleanField(label='Souvlaki',required=False)
