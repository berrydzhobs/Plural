"""Streame URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

#Start My imports static files 
from django.conf import settings
from django.conf.urls.static import static
#End my static files imports
admin.site.site_header = "Plural"
admin.site.site_title = "Plural"
admin.site.index_title = "Darshboard Portal"

urlpatterns = [
    path('00-0-00/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('Content.urls')),
    path('', include('Main.urls')),
    path('', include('Startqt.urls')),
    path('', include('Profile.urls')),
    path('', include('Feed.urls')),
    path('', include('Discover.urls')),
    path('', include('Setting.urls')),
    path('', include('Graph.urls')),
    path('', include('Document.urls')),
    path('', include('Search.urls')),
    path('accounts/', include('allauth.urls')),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)