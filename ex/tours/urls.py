from . import views
from django.conf.urls import url,include
from django.views.generic import ListView,TemplateView
from models import image
from views import photo

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^thematic/',views.thematic,name='thematic'),
    url(r'^classics/',views.Classic,name='classic'),
    url(r'^classics_private/',views.Classic_private,name='classic_private'),
    url(r'^classics_group/',views.Classic_group,name='classic_group'),
    url(r'^bus/',views.Bus,name='bus'),
    url(r'^bus_private/',views.Bus_private,name='bus_private'),
    url(r'^bus_group/',views.Bus_group,name='bus_group'),
    url(r'^cruises/',views.Cruises,name='cruises'),
    url(r'^cruises_private/',views.Cruises_private,name='cruises_private'),
    url(r'^cruises_group/',views.Cruises_group,name='cruises_group'),
    url(r'^bicycle/',views.Bicycle,name='bicycle'),
    url(r'^bicycle_private/',views.Bicycle_private,name='bicycle_private'),
    url(r'^bicycle_group/',views.Bicycle_group,name='bicycle_group'),
    url(r'^excursions/',views.Excursions,name='excursions'),
    url(r'^excursions_private/',views.Excursions_private,name='excursions_private'),
    url(r'^excursions_group/',views.Excursions_group,name='excursions_group'),
    url(r'^thematic_kids_and_family/',views.Thematic_Kids_And_Family,name='thematic_kids_and_family'),
    url(r'^thematic_kids_and_family_private/',views.Thematic_Kids_And_Family_private,name='thematic_kids_and_family_private'),
    url(r'^thematic_kids_and_family_group/',views.Thematic_Kids_And_Family_group,name='thematic_kids_and_family_group'),
    url(r'^thematic_gastronomy/',views.Thematic_Gastronomy,name='thematic_gastronomy'),
    url(r'^thematic_gastronomy_private/',views.Thematic_Gastronomy_private,name='thematic_gastronomy_private'),
    url(r'^thematic_gastronomy_group/',views.Thematic_Gastronomy_group,name='thematic_gastronomy_group'),
    url(r'^thematic_photo/',views.Thematic_Photo,name='thematic_photo'),
    url(r'^thematic_photo_private/',views.Thematic_Photo_private,name='thematic_photo_private'),
    url(r'^thematic_photo_group/',views.Thematic_Photo_group,name='thematic_photo_group'),
    url(r'^thematic_street_art/',views.Thematic_Street_Art,name='thematic_street_art'),
    url(r'^thematic_street_art_private/',views.Thematic_Street_Art_private,name='thematic_street_art_private'),
    url(r'^thematic_street_art_group/',views.Thematic_Street_Art_group,name='thematic_street_art_group'),
    url(r'^thematic_political/',views.Thematic_Political,name='thematic_political'),
    url(r'^thematic_political_private/',views.Thematic_Political_private,name='thematic_political_private'),
    url(r'^thematic_political_group/',views.Thematic_Political_group,name='thematic_political_group'),
    url(r'^thematic_segway/',views.Thematic_Segway,name='thematic_segway'),
    url(r'^thematic_segway_private/',views.Thematic_Segway_private,name='thematic_segway_private'),
    url(r'^thematic_segway_group/',views.Thematic_Segway_group,name='thematic_segway_group'),
    url(r'^anazhthsh/',views.search_result,name='search_result'),
    url(r'^(?P<q>\d+)$',photo.as_view()),
]
