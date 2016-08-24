from __future__ import unicode_literals
from math import radians, cos, sin, asin, sqrt
from django.db import models

# Create your models here.


class Shop(models.Model):
    name = models.CharField(max_length=128, unique=False)
    perioxh=models.CharField(max_length=128, unique=False,blank=True)
    periferia=models.CharField(max_length=128, unique=False,blank=True)
    dieuthinsh=models.CharField(max_length=128, unique=False,blank=True)
    stigma=models.URLField(blank=True)
    butlair_link=models.URLField(blank=True)
    site=models.URLField(blank=True)
    thl_mail=models.CharField(max_length=128, unique=False,blank=True)
    perigrafh=models.TextField(blank=True)
    wrario=models.TextField(blank=True)
    greek_design=models.NullBooleanField()
    handmade=models.NullBooleanField()
    not_expensive=models.NullBooleanField()
    gift=models.NullBooleanField()
    traditional=models.NullBooleanField()
    kids=models.NullBooleanField()
    men=models.NullBooleanField()
    women=models.NullBooleanField()
    ceramics=models.NullBooleanField()
    logo = models.FileField(upload_to="shopping/static/shopping/img/logo",null=True, blank=True)
    photo = models.FileField(upload_to="shopping/static/shopping/img/photo",null=True, blank=True)
    latitude = models.FloatField(null=True,blank=True)
    longitude = models.FloatField(null=True,blank=True)
