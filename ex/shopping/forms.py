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

class Kind_of_shop(forms.Form):
        souvenir = forms.BooleanField(label='Σουβενίρ',required=False)
        delicatessen = forms.BooleanField(label='Delicatessen',required=False)
        kosmhmata = forms.BooleanField(label='Κοσμήματα',required=False)
        moda = forms.BooleanField(label='Μόδα',required=False)
        


class Tags(forms.Form):
        greek_design = forms.BooleanField(label='Greek Design',required=False)
        handmade = forms.BooleanField(label='Handmade',required=False)
        not_expensive = forms.BooleanField(label='Not Expensive',required=False)
        gift = forms.BooleanField(label='Gift',required=False)
        kids = forms.BooleanField(label='Kids',required=False)
        traditional = forms.BooleanField(label='Traditional',required=False)
        men = forms.BooleanField(label='Men',required=False)
        women = forms.BooleanField(label='Women',required=False)
        ceramics = forms.BooleanField(label='Ceramics',required=False)
        



