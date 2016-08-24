from django.conf.urls import url,include
from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^tours/',include('tours.urls')),
    url(r'^rests/',include('search_engine.urls')),
    url(r'^shopping/',include('shopping.urls')),
    url(r'^cafe_bars/',include('cafe_bars.urls')),
    
]
