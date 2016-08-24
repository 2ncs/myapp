from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Tour(models.Model):
    
    PRIVATE_GROUP_CHOICES = (
        ("PRIVATE","private"),
        ("GROUP","group")
        )
    name = models.CharField(max_length=128, unique=False)
    perigrafh = models.TextField(blank=True)
    timetable = models.TextField(blank=True)
    diarkeia = models.CharField(max_length=128, unique=False,blank=True)
    kostos = models.CharField(max_length=128, unique=False,blank=True)
    private_group = models.CharField(max_length=30, unique=False,blank=True,choices=PRIVATE_GROUP_CHOICES)
    logo = models.FileField(upload_to="tours/static/tours/img/logo",null=True, blank=True)
    photo = models.FileField(upload_to="tours/static/tours/img/photo",null=True, blank=True)
    category = models.CharField(max_length=128, unique=False,blank=True)
    site = site=models.URLField(blank=True)
    
    def __unicode__(self):
        data=self.name
        return data


#####THEMATIKA#####

class image(models.Model):
    name=models.ForeignKey(Tour, on_delete=models.CASCADE)
    photo= models.FileField(upload_to="tours/static/tours/img/photo")

    def __unicode__(self):
        data=self.name.name
        return data



class thematic_kids_and_family(models.Model):
    name=models.ForeignKey(Tour, on_delete=models.CASCADE)

    def __unicode__(self):
        data=self.name.name
        return data
    
    
class thematic_gastronomy(models.Model):
    name=models.ForeignKey(Tour, on_delete=models.CASCADE)

    def __unicode__(self):
        data=self.name.name
        return data



class thematic_photo(models.Model):
    name=models.ForeignKey(Tour, on_delete=models.CASCADE)

    def __unicode__(self):
        data=self.name.name
        return data


class thematic_street_art(models.Model):
    name=models.ForeignKey(Tour, on_delete=models.CASCADE)

    def __unicode__(self):
        data=self.name.name
        return data


class thematic_political(models.Model):
    name=models.ForeignKey(Tour, on_delete=models.CASCADE)

    def __unicode__(self):
        data=self.name.name
        return data


class thematic_segway(models.Model):
    name=models.ForeignKey(Tour, on_delete=models.CASCADE)

    def __unicode__(self):
        data=self.name.name
        return data

#########################################################

class classic(models.Model):
    name=models.ForeignKey(Tour, on_delete=models.CASCADE)

    def __unicode__(self):
        data=self.name.name
        return data


class bus(models.Model):
    name=models.ForeignKey(Tour, on_delete=models.CASCADE)

    def __unicode__(self):
        data=self.name.name
        return data    

class cruises(models.Model):
    name=models.ForeignKey(Tour, on_delete=models.CASCADE)

    def __unicode__(self):
        data=self.name.name
        return data



class bicycle(models.Model):
    name=models.ForeignKey(Tour, on_delete=models.CASCADE)

    def __unicode__(self):
        data=self.name.name
        return data



class excursions(models.Model):
    name=models.ForeignKey(Tour, on_delete=models.CASCADE)

    def __unicode__(self):
        data=self.name.name
        return data

    

    
