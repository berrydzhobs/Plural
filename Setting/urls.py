from django.contrib import admin
from django.urls import path,include

#Start My imports static files 
from django.conf import settings
from django.conf.urls.static import static
#End my static files imports

from . import views


urlpatterns = [
    path('accounts/settings/',views.settings,name='settings'),
    path('accounts/settings/delete-account/', views.delete_account, name='delete-settings'),
    path('accounts/settings/update-account/', views.update_account, name='general-settings'),
    path('accounts/settings/change-email/', views.change_email, name='change_email'),
    path('accounts/settings/verify-email/', views.verify_email, name='verify_email'),
    path('accounts/settings/change-password/', views.change_password, name='security-settings'),
    path('update_profile/', views.update_profile, name='update_profile'),
]