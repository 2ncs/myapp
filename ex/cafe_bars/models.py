from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Cafe_Bar(models.Model):
    name = models.CharField(max_length=128, unique=False)
    dieuthinsh = models.CharField(max_length=128, unique=False)
    perioxh = models.CharField(max_length=128, unique=False)
    thl=models.CharField(max_length=128, unique=False)
    perigrafh = models.TextField(blank=True)
    logo = models.FileField(upload_to="cafe_bars/static/cafe_bars/img/logo",null=True, blank=True)
    photo = models.FileField(upload_to="cafe_bars/static/cafe_bars/img/photo",null=True, blank=True)
    site=models.URLField(blank=True)
    butlair_link=models.URLField(blank=True)
    roof=models.NullBooleanField()
    garden=models.NullBooleanField()
    romantic=models.NullBooleanField()
    view=models.NullBooleanField()
    gay_lesbian=models.NullBooleanField()
    dance=models.NullBooleanField()
    rock=models.NullBooleanField()
    techno=models.NullBooleanField()
    rempetiko_ellhniko=models.NullBooleanField()
    jazz=models.NullBooleanField()
    chill=models.NullBooleanField()
    whiskes=models.NullBooleanField()
    mpouzoukia=models.NullBooleanField()
    live_music=models.NullBooleanField()
    beach_bar=models.NullBooleanField()
    latitude = models.FloatField(null=True,blank=True)
    longitude = models.FloatField(null=True,blank=True)

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

    def __unicode__(self):
        data=self.name
        return data


##################################################

class Club(models.Model):
    name=models.ForeignKey(Cafe_Bar, on_delete=models.CASCADE)
    def __unicode__(self):
        data=self.name.name
        return data    


class Bar(models.Model):
    name=models.ForeignKey(Cafe_Bar, on_delete=models.CASCADE)
    def __unicode__(self):
        data=self.name.name
        return data    


class Cafe(models.Model):
    name=models.ForeignKey(Cafe_Bar, on_delete=models.CASCADE)
    def __unicode__(self):
        data=self.name.name
        return data    


class Cocktail_bar(models.Model):
    name=models.ForeignKey(Cafe_Bar, on_delete=models.CASCADE)
    def __unicode__(self):
        data=self.name.name
        return data



class Wine_bar(models.Model):
    name=models.ForeignKey(Cafe_Bar, on_delete=models.CASCADE)
    def __unicode__(self):
        data=self.name.name
        return data    


    
class Beer_pub(models.Model):
    name=models.ForeignKey(Cafe_Bar, on_delete=models.CASCADE)
    def __unicode__(self):
        data=self.name.name
        return data    



