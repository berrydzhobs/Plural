from django.contrib import admin
from django.urls import path,include

#Start My imports static files 
from django.conf import settings
from django.conf.urls.static import static
#End my static files imports

from . import views



urlpatterns = [
    path('', views.cornical_feed.as_view(), name='feed'),
]

htmx_urlpatterns = [
    
]

urlpatterns += htmx_urlpatterns