from django.contrib import admin
from django.urls import path,include

#Start My imports static files 
from django.conf import settings
from django.conf.urls.static import static
#End my static files imports

from . import views


urlpatterns = [
    path('documents/terms/',views.Terms,name='terms'),
    path('documents/privacy/',views.Privacy,name='privacy'),
    path('documents/cookie-policy/',views.CookiePolicy,name='cookie-policy'),
    path('documents/disclaimer/',views.Disclaimer,name='disclaimer'),
]