# -*- coding: utf-8 -*-

from django.utils.safestring import mark_safe
from django import forms
from .models import *


class HorizRadioRenderer(forms.RadioSelect.renderer):
    """ this overrides widget method to put radio buttons horizontally
        instead of vertically.
    """
    def render(self):
            """Outputs radios"""
            return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))


class search(forms.Form):
        onoma = forms.CharField(label='Αναζήτηση', max_length=128,required=False,widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))


class radio(forms.Form):
        CHOICES=[('GROUP','Group'),
         ('PRIVATE','Private'),
         ('ALL','All')
                 ]

        choice = forms.ChoiceField(label='Private/Group  :',choices=CHOICES, widget=forms.RadioSelect(renderer=HorizRadioRenderer))


