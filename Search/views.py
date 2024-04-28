from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from Content.models import App
from Profile.models import Profile
from .models import SearchKeyword
from django.conf import settings
import json
from django.core.paginator import Paginator
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import random
from django.db.models import Q
from django.db.models import Count
randomc =[
{
    'color1': '/static/images/login/1.jpg'
},
{
    'color1': '/static/images/login/2.jpg'
},
{
    'color1': '/static/images/login/3.jpg'
},
{
    'color1': '/static/images/login/4.jpg'
}
]
class Start(View):
    def get(self, request, *args, **kwargs):
        bg = random.choices(randomc, k=1)
        context = {
            'color' : bg,
        }

        return render(request, 'Search/start.html', context)

class MainSearch(View):

    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('qt')
        # Search for users and tags that match the query
        if query:
            apps = App.objects.filter(Q(name__icontains=query))

        results = []
        for app in apps:
            results.append(('post', app))

        context = {
            'results': results,
            'query': query,
        }

        return render(request, 'Search/result.html', context)
