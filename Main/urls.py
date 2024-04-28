from django.contrib import admin
from django.urls import path,include

#Start My imports static files 
from django.conf import settings
from django.conf.urls.static import static
#End my static files imports
from django.contrib.sitemaps.views import sitemap
from .sitemaps import Appsitemap, Startpage
from Main.views import robots_txt
from Main.views import ads_txt

from . import views


sitemaps = {
    'blog': Appsitemap,
    'static':Startpage
}

urlpatterns = [
   path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
   path("main/robots.txt", robots_txt),
   path("ads.txt", ads_txt),
   #
   path('menu/',views.menu,name='menu'),
   path('account/flw/logout/', views.logout,name='logout'),
]