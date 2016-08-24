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

class Kind_of_bar(forms.Form):
        club = forms.BooleanField(label='Club',required=False)
        bar = forms.BooleanField(label='Bar',required=False)
        cafe = forms.BooleanField(label='Cafe',required=False)
        cocktail_bar = forms.BooleanField(label='Cocktail Bar',required=False)
        wine_bar= forms.BooleanField(label='Wine Bar',required=False)
        beer_pu=forms.BooleanField(label='Beer Pub',required=False)


class Tags(forms.Form):
        roof = forms.BooleanField(label='Roof',required=False)
        garden = forms.BooleanField(label='Garden',required=False)
        romantic = forms.BooleanField(label='Romantic',required=False)
        view = forms.BooleanField(label='View',required=False)
        gay_lesbian = forms.BooleanField(label='Gay/Lesbian',required=False)
        dance = forms.BooleanField(label='Dance',required=False)
        rock = forms.BooleanField(label='Rock',required=False)
        techno = forms.BooleanField(label='Techno',required=False)
        rempetiko_ellhniko = forms.BooleanField(label='Ρεμπέτικο-Ελληνικό-Λαϊκό',required=False)
        jazz = forms.BooleanField(label='Jazz',required=False)
        chill = forms.BooleanField(label='Chill',required=False)
        whiskes = forms.BooleanField(label='Whiskes',required=False)
        mpouzoukia = forms.BooleanField(label='Μπουζούκια',required=False)
        live_music = forms.BooleanField(label='Live Music',required=False)
        beach_bar = forms.BooleanField(label='Beach Bar',required=False)



