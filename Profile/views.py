from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from Content.models import App
from Profile.models import Profile, ProfileFollow
from django.db.models import Q
from django.conf import settings
import json
from django.core.paginator import Paginator
from django.views import View
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserChangeForm
from .forms import*
from django.apps import apps
App = apps.get_model('Content', 'App')

pqt = 1

import random


#==========================Discover=====================================

discover_randow_colors =[
{
    'color': '#003dff'
},
{
    'color':'#7e9e00'
},
{
    'color':'#ffa600'
},
{
    'color':'#c9a45d'
}
]

randomc =[
{
    'color1': 'bg-primary'
},
{
    'color1':'bg-yellow'
},
{
    'color1':'bg-red'
},
{
    'color1':'bg-gradient-dark'
}
]

# Views for profile related stuffs.
#==========================Profile=====================================

def profile_view(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    posts = App.objects.filter(user=profile.user)
    if request.user.is_authenticated:
        is_following = False
        if request.user.is_authenticated:
            is_following = ProfileFollow.objects.filter(follower=request.user, following=profile.user).exists()
        #
        follow_back = ProfileFollow.objects.filter(follower=profile.user, following=request.user).exists()
        
        # Pagination start here
        paginator = Paginator(posts, 3)
        page = request.GET.get('page', 1)

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        context = {
                'profile': profile,
                'posts': posts,
                'is_following': is_following,
                'follow_back': follow_back,
            }
        if request.htmx:
            return render(request, 'Profile/Include/grid.html', context)
        else:
            return render(request, 'Profile/profiler.html', context)
    else:
        # Pagination start here
        paginator = Paginator(posts, 3)
        page = request.GET.get('page', 1)

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        context = {
                'profile': profile,
                'posts': posts,
            }
        if request.htmx:
            return render(request, 'Profile/Include/grid.html', context)
        else:
            return render(request, 'Profile/profiler.html', context)





def edit_profile(request):
    user = request.user
    profile = user.profile

    if request.method == 'POST':
        user_form = FirstNameForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile', username=request.user.username)
    else:
        user_form = FirstNameForm(instance=user)
        profile_form = ProfileForm(instance=profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'Profile/Update/userimage.html', context)






class AddFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        profile.followers.add(request.user)
        notification = Notification.objects.create(notification_type=3, from_user=request.user, to_user=profile.user)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

class RemoveFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        profile.followers.remove(request.user)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def follow_user(request, username):
    follower = request.user
    following_user = get_object_or_404(User, username=username)
    following_profile = Profile.objects.get(user=following_user)

    if follower == following_user:
        # A user cannot follow themselves
        return redirect('profile', username=username)

    # Create a new Follow object if it doesn't exist
    follow, created = ProfileFollow.objects.get_or_create(
        follower=follower,
        following=following_user,
    )
    # Create the Object instance
    obj = NotificationObject.objects.create(follow=follow, user=follower)

    # Create the Target instance
    target = NotificationTarget.objects.create(follow=follow, user=following_user)

    # Create the notification
    Notification.objects.create(
        receiver=following_user,
        sender=follower,
        message='Started following you',
        action_object=obj,
        target=target
    )

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def unfollow(request, username):
    # Get the User object of the person being followed
    user_to_unfollow = get_object_or_404(User, username=username)

    # Check if the user is already following the user_to_unfollow
    follow = ProfileFollow.objects.filter(follower=request.user, following=user_to_unfollow)
    if follow.exists():
        follow.delete()
        messages.success(request, f"You have unfollowed {user_to_unfollow.username}.")
    else:
        messages.error(request, f"You were not following {user_to_unfollow.username}.")

    # Redirect to the user's profile page
    return HttpResponseRedirect(request.META['HTTP_REFERER'])