from django.contrib import admin
from django.urls import path,include

#Start My imports static files 
from django.conf import settings
from django.conf.urls.static import static
#End my static files imports

from . import views


urlpatterns = [
    path('search/',views.Start.as_view(),name='search'),
    path('search/i/',views.MainSearch.as_view(),name='mainsearch')
    ]