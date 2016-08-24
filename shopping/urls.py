from django.conf.urls import url,include
from . import views
# We are adding a URL called
urlpatterns = [
    url(r'^', views.index, name='index'),
    
    
]
