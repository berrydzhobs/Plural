from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from Profile.models import Profile
from django.conf import settings
import json
from django.core.paginator import Paginator
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy


#Terms
#=========================================================
def Terms(request,*args,**kwargs):
    return render(request,"Document/terms.html")

#Privacy
#=========================================================
def Privacy(request,*args,**kwargs):
    return render(request,"Document/privacy.html")

#CookiePolicy
#=========================================================
def CookiePolicy(request,*args,**kwargs):
    return render(request,"Document/cookie.html")

#Disclaimer
#=========================================================
def Disclaimer(request,*args,**kwargs):
    return render(request,"Document/disclaimer.html")