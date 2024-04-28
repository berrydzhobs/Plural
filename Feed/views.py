from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from Profile.models import Profile
from Content.models import App
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.views.generic import ListView
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
import json
import sys
import random


from django.db.models import Q, Subquery, OuterRef

from Graph.models import Topic


randomc =[
{
    'color1': '/static/images/home/1.svg',
    'color':'yellow'
},
{
    'color1': '/static/images/home/2.png',
    'color':'#603b45 0%, #ff9900 100%'
},
{
    'color1': '/static/images/home/3.png',
    'color':'linear-gradient(#603b45 0%, #ff9900 100%)'
},
{
    'color1': '/static/images/home/4.png',
    'color':'linear-gradient(#000000 0%, #ffb100 100%)'
},
{
    'color1': '/static/images/home/5.png',
    'color':'linear-gradient(#46a329 0%, #0093ff 100%)'
},
{
    'color1': '/static/images/home/6.png',
    'color':'linear-gradient(#603b45 0%, #ff9900 100%)'
},
{
    'color1': '/static/images/home/7.png',
    'color':'linear-gradient(#603b45 0%, #ff9900 100%)'
}
]

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



class cornical_feed(View):
    def get(self, request, *args, **kwargs):
        bg = random.choices(randomc, k=1)
        recent_posts = App.objects.all().order_by('-created_at')[0:1]
        posts = App.objects.all().exclude(pinned = True).order_by('-created_at')[0:12]
        topics = Topic.objects.all().order_by('-created_at')[0:12]
        editor_picks = App.objects.filter(pinned = True).order_by('-created_at')[0:4]

        context = {
            'posts': posts,
            'recent_posts': recent_posts,
            'topics': topics,
            'editor_picks': editor_picks,
            'color': bg,
        }

        return render(request, 'Feed/feed.html', context)