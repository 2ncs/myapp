from . import views
from django.conf.urls import url,include

urlpatterns = [
    url(r'^$',views.index,name='index'),
    #url(r'^thanks/$',views.index,name='index'),
    #url(r'^insert$',views.index_ins,name='insert_ins'),
    url(r'^insert/$',views.index_ins,name='index_ins'),
    url(r'^results/$',views.index,name='index'),
    
]
