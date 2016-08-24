from __future__ import unicode_literals
from math import radians, cos, sin, asin, sqrt
from django.db import models

# Create your models here.


class Rests(models.Model):
    PRICE_CHOICES = (
        ("-10","ews 10 eurw"),
        ("10-20","10 me 20 eurw"),
        ("20-30","20 me 30 eurw"),
        ("30-40","30 me 40 eurw"),
        ("40-50","40 me 50 eurw"),
        ("50-","50 eurw kai panw")
        )

    name = models.CharField(max_length=128, unique=False)
    perioxh=models.CharField(max_length=128, unique=False,blank=True)
    periferia=models.CharField(max_length=128, unique=False,blank=True)
    dieuthinsh=models.CharField(max_length=128, unique=False,blank=True)
    price=models.CharField(max_length=30, unique=False,blank=True,choices=PRICE_CHOICES)
    live_mousikh=models.NullBooleanField()
    for_kids=models.NullBooleanField()
    view=models.NullBooleanField()
    romantic=models.NullBooleanField()
    cozy=models.NullBooleanField()
    stigma=models.URLField(blank=True)
    butlair_link=models.URLField(blank=True)
    site=models.URLField(blank=True)
    e_table=models.NullBooleanField()
    thl=models.CharField(max_length=128, unique=False,blank=True)
    comments=models.TextField(blank=True)
    rate=models.FloatField(null=True,blank=True)
    latitude = models.FloatField(null=True,blank=True)
    longitude = models.FloatField(null=True,blank=True)

    
    def __unicode__(self):
        #data=[self.name,self.perioxh]
        data=self.id
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
 



class Bar_Restaurant(models.Model):
    name=models.ForeignKey(Rests, on_delete=models.CASCADE)
    def __unicode__(self):
        data=self.name.id
        return data
    
class Brunch(models.Model):
    name=models.ForeignKey(Rests, on_delete=models.CASCADE)

    def __unicode__(self):
        data=self.name.id
        return data
#########Street Food#######################

class Souvlaki(models.Model):
    name=models.ForeignKey(Rests, on_delete=models.CASCADE)

    def __unicode__(self):
        data=self.name.id
        return data

class Falafes(models.Model):
    name=models.ForeignKey(Rests, on_delete=models.CASCADE)

    def __unicode__(self):
        data=self.name.id
        return data
    
class Lagmatzoun(models.Model):
    name=models.ForeignKey(Rests, on_delete=models.CASCADE)

    def __unicode__(self):
        data=self.name.id
        return data

class Sandwitch(models.Model):
    name=models.ForeignKey(Rests, on_delete=models.CASCADE)

    def __unicode__(self):
        data=self.name.id
        return data

class Krepa(models.Model):
    name=models.ForeignKey(Rests, on_delete=models.CASCADE)

    def __unicode__(self):
        data=self.name.id
        return data

class Kotompoukies(models.Model):
    name=models.ForeignKey(Rests, on_delete=models.CASCADE)

    def __unicode__(self):
        data=self.name.id
        return data

class Mpougatsa_Sfoliata(models.Model):
    name=models.ForeignKey(Rests, on_delete=models.CASCADE)

    def __unicode__(self):
        data=self.name.id
        return data


class Burger(models.Model):
    name=models.ForeignKey(Rests, on_delete=models.CASCADE)

    def __unicode__(self):
        data=self.name.id
        return data
##################################################################

class Mezedopoleia(models.Model):
    name=models.ForeignKey(Rests, on_delete=models.CASCADE)

    def __unicode__(self):
        data=self.name.id
        return data


class Fusion(models.Model):
    name=models.ForeignKey(Rests, on_delete=models.CASCADE)

    def __unicode__(self):
        data=self.name.id
        return data


class Ellhnikh_Paradosiakh(models.Model):
    name=models.ForeignKey(Rests, on_delete=models.CASCADE)

    def __unicode__(self):
        data=self.name.id
        return data


class Burger_Amerikanikh(models.Model):
    name=models.ForeignKey(Rests, on_delete=models.CASCADE)

    def __unicode__(self):
        data=self.name.id
        return data


class Vegeterian(models.Model):
    name=models.ForeignKey(Rests, on_delete=models.CASCADE)

    def __unicode__(self):
        data=self.name.id
        return data

class Fish(models.Model):
    name=models.ForeignKey(Rests, on_delete=models.CASCADE)

    def __unicode__(self):
        data=self.name.id
        return data


class Mesogeiakh(models.Model):
    name=models.ForeignKey(Rests, on_delete=models.CASCADE)

    def __unicode__(self):
        data=self.name.id
        return data

class Sigxronh_Ellhnikh(models.Model):
    name=models.ForeignKey(Rests, on_delete=models.CASCADE)

    def __unicode__(self):
        data=self.name.id
        return data


class Indikh(models.Model):
    name=models.ForeignKey(Rests, on_delete=models.CASCADE)

    def __unicode__(self):
        data=self.name.id
        return data

class Gallikh(models.Model):
    name=models.ForeignKey(Rests, on_delete=models.CASCADE)

    def __unicode__(self):
        data=self.name.id
        return data
    
class Italikh(models.Model):
    name=models.ForeignKey(Rests, on_delete=models.CASCADE)

    def __unicode__(self):
        data=self.name.id
        return data

class Multi_Ethnic(models.Model):
    name=models.ForeignKey(Rests, on_delete=models.CASCADE)

    def __unicode__(self):
        data=self.name.id
        return data

class Afrikanikh(models.Model):
    name=models.ForeignKey(Rests, on_delete=models.CASCADE)

    def __unicode__(self):
        data=self.name.id
        return data


class Sushi(models.Model):
    name=models.ForeignKey(Rests, on_delete=models.CASCADE)

    def __unicode__(self):
        data=self.name.id
        return data

class Ispanikh(models.Model):
    name=models.ForeignKey(Rests, on_delete=models.CASCADE)

    def __unicode__(self):
        data=self.name.id
        return data


class Latin(models.Model):
    name=models.ForeignKey(Rests, on_delete=models.CASCADE)

    def __unicode__(self):
        data=self.name.id
        return data

class Sigxronh(models.Model):
    name=models.ForeignKey(Rests, on_delete=models.CASCADE)

    def __unicode__(self):
        data=self.name.id
        return data


class Politikh(models.Model):
    name=models.ForeignKey(Rests, on_delete=models.CASCADE)

    def __unicode__(self):
        data=self.name.id
        return data

class Asiatikh(models.Model):
    name=models.ForeignKey(Rests, on_delete=models.CASCADE)

    def __unicode__(self):
        data=self.name.id
        return data


class Glyko(models.Model):
    name=models.ForeignKey(Rests, on_delete=models.CASCADE)

    def __unicode__(self):
        data=self.name.id
        return data


class Pagwto(models.Model):
    name=models.ForeignKey(Rests, on_delete=models.CASCADE)

    def __unicode__(self):
        data=self.name.id
        return data

    


    






    



    






    



    







    



    

















    

    


    

    


    

    


    


    



    



    


    



    


    




    













    
