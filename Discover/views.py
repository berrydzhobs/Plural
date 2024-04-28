from django.shortcuts import render, HttpResponse,redirect,get_object_or_404
from Content.models import App
from Graph.models import Topic
from django.contrib.auth.models import User
from Profile.models import Profile, ProfileFollow
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import json
from django import forms
import random
from random import sample
from django.views import View
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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




broadcasts_cat =[
{
    'name': 'News & Politics',
    'slug': 'news-and-politics',
    'thumbnail' : '/static/images/web/1.png',
    'description' : 'DJANGO_SETTINGS_MODULE'
},
{
    'cat':'bg-yellow'
},
{
    'cat':'bg-red'
},
{
    'cat':'bg-gradient-dark'
}
]



def discover(request):
    users = User.objects.all()
    user_posts = []
    for user in users:
        posts = App.objects.filter(user=user).order_by('-created_at')[:3]
        user_posts.append({'user': user, 'posts': posts})
    #
    topic = Topic.objects.all()
    latest = App.objects.all().order_by('-created_at')[:3]

    following_users = ProfileFollow.objects.filter(follower=user).select_related('following__profile').values_list('following', flat=True)
    people = Profile.objects.exclude(user__in=following_users).exclude(user=user)
    people = sample(list(people), min(4, len(people)))[:3]

    # Pagination start here
    paginator = Paginator(topic, 6)
    page = request.GET.get('page', 1)

    try:
        topic = paginator.page(page)
    except PageNotAnInteger:
        topic = paginator.page(1)
    except EmptyPage:
        topic = paginator.page(paginator.num_pages)
    context = {
    'user_posts': user_posts,
    'cat': topic,
    'latest': latest,
    'people': people,
    }
    if request.htmx:
        return render(request, 'Discover/tag_data.html', context)
    else:
        return render(request, 'Discover/discover.html', context)

def topicdetail(request, order_id=None):
    category = None
    color = random.choices(discover_randow_colors, k=1)
    cover = App.objects.all().order_by('?')[:1]
    posts = App.objects.all()
    topic = Topic.objects.all()
    if order_id:
        category = get_object_or_404(Topic, order_id=order_id)
        posts = posts.filter(topic__exact=category)
        topic = topic.filter(parent__exact=category)
    paginator = Paginator(posts, 50)
    page = request.GET.get('page', 1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
            'category':category,
            'cover':cover,
            'posts':posts,
            'color':color,
            'topics':topic,
        }

    return render(request, 'Discover/topic.html', context)