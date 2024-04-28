from django.contrib import admin
from django.urls import path,include

#Start My imports static files 
from django.conf import settings
from django.conf.urls.static import static
#End my static files imports
from . import views



urlpatterns = [
    path('u/<str:username>/', views.profile_view, name='profile'),
    #
    path('profile/<int:pk>/followers/add', views.AddFollower.as_view(), name='add-follower'),
    path('profile/<int:pk>/followers/remove', views.RemoveFollower.as_view(), name='remove-follower'),
    #
    path('edit/it/', views.edit_profile, name='edit_profile'), 
    path('follow/<str:username>/', views.follow_user, name='follow'),
    path('unfollow/<str:username>/', views.unfollow, name='unfollow'),
]