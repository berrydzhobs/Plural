from django.contrib import admin
from django.urls import path,include

#Start My imports static files 
from django.conf import settings
from django.conf.urls.static import static
#End my static files imports
from . import views

from django.contrib.sitemaps.views import sitemap
from .sitemaps import AppSitemap

sitemaps = {
    
    "posts": AppSitemap,
}


urlpatterns = [
    #Create Update Watch and Delete Video
    path('contents/sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path("contents/sitemap-posts.xml", sitemap, {"sitemaps": {"posts": AppSitemap}}, name="django.contrib.sitemaps.views.sitemap"),
    #
    path('<slug:order_id>',views.PostDetailView_one.as_view(),name='post_detail'),
    path('<str:username>/web/application/<slug:order_id>/', views.PostDetailView.as_view(), name='post'),
]