from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from Profile.models import Profile, ProfileInterest
from Content.models import Topic
from django.conf import settings
import json
from django.core.paginator import Paginator
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.decorators.http import require_GET
from .forms import *

@require_GET
def robots_txt(request):
    lines = [
        # Group 1 - Google
        "User-Agent: Googlebot",
        "Allow: /read/",
        "Disallow: actvties/",
        "Disallow: /junk/",

        # Group 1 - Yandex
        "User-Agent: Yandexbot",
        "Disallow: /private/",
        "Disallow: /junk/",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


@require_GET
def ads_txt(request):
    lines = [
        # Group 1 - Google Ads
        "google.com, pub-7637919407359447, DIRECT, f08c47fec0942fa0",

        # Group 1 - Yandex
        #"User-Agent: Yandexbot",
        #"Disallow: /private/",
        #"Disallow: /junk/",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")



def menu(request,*args,**kwargs):
    return render(request,"Main/menu.html")


#Logout

def logout(request):
    auth.logout(request)
    messages.success(request, f'Thanks for spending some quality time with us🖐. have a great time 🤙!')
    return HttpResponseRedirect(request.META['HTTP_REFERER']) 