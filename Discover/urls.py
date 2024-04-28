from django.contrib import admin
from django.urls import path,include

#Start My imports static files 
from django.conf import settings
from django.conf.urls.static import static
#End my static files imports

from . import views


#Authentication Patterns
# Login - Registration(Create Account) - Password Recovery

urlpatterns = [
    path('discover/',views.discover,name='discover'),
    #
    path('discover/<slug:order_id>/',views.topicdetail,name='topic'),
]