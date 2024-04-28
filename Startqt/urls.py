from django.urls import path,include

#Start My imports static files 
from django.conf import settings
from django.conf.urls.static import static
#End my static files imports


from . import views


urlpatterns = [
    path('about/',views.about.as_view(),name='about'),
    path('contact/',views.contact,name='contact')

]