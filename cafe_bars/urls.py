from django.conf.urls import url,include
from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^results/$', views.index, name='index'),
    
    
]
