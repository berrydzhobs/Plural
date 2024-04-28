from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from Content.models import App
from Profile.models import Profile
from django.conf import settings
import json
from django.core.paginator import Paginator
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import random
pqt = 1
# Views for profile related stuffs.
#==========================Profile=====================================


#{Loading page}#
#==============
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


#About page
#==========#

class about(ListView):
    model = User
    template_name = 'Startqt/About.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all Video by user
        return context



#Contact Us page
#==================#

def contact(request):
	return render(request,"Startqt/Contact.html")

