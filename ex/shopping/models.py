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


    def __unicode__(self):
        #data=[self.name,self.perioxh]
        data=self.name
        return data

    def distance(self,lon1,lat1):
        lon2=self.longitude
        lat2=self.latitude
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        # haversine formula 
        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a)) 
        km = 6367 * c
        return km


class Souvenir(models.Model):
    name=models.ForeignKey(Shop, on_delete=models.CASCADE)
    def __unicode__(self):
        data=self.name.name
        return data
    

class Delicatessen(models.Model):
    name=models.ForeignKey(Shop, on_delete=models.CASCADE)
    def __unicode__(self):
        data=self.name.name
        return data

class Kosmhma(models.Model):
    name=models.ForeignKey(Shop, on_delete=models.CASCADE)
    def __unicode__(self):
        data=self.name.name
        return data


class Moda(models.Model):
    name=models.ForeignKey(Shop, on_delete=models.CASCADE)
    def __unicode__(self):
        data=self.name.name
        return data







