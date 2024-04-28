from django.shortcuts import render,HttpResponse,redirect, get_object_or_404
from Graph.models import Topic
from django.contrib import messages
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django import forms
from django.http import HttpResponseRedirect, HttpResponse
import json
from django.http import JsonResponse
from .forms import *
import random
import time
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.http import require_GET
from django.views.generic import FormView
from django.forms import modelformset_factory

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from PIL import Image
import uuid




@require_GET
def robots_txt(request):
    lines = [
        # Group 1 - General
        "User-Agent: * ",
        "Allow: /genre/",
        "Allow: /read/",
        "Allow: /collection/",
        "Disallow: /cntnts/",

        # Group 1 - Google
        "User-Agent: Googlebot",
        "Allow: /genre/",
        "Allow: /read/",
        "Allow: /collection/",
        "Disallow: /cntnts/",

        # Group 1 - Yandex
        "User-Agent: Yandexbot",
        "Allow: /genre/",
        "Allow: /read/",
        "Allow: /collection/",
        "Disallow: /cntnts/",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

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

class PostDetailView(View):
    def get(self, request, username, order_id, *args, **kwargs):
        user = request.user
        post = App.objects.get(user__username=username, order_id=order_id)
        qs = json.dumps(list(App.objects.values()) ,default=str)
        color = random.choices(discover_randow_colors, k=1)
        
        context = {
            'post': post,
            'color':color,
        }
        return render(request, 'Content/Detail/post_detail.html', context)



class PostDetailView_one(View):
    def get(self, request, order_id, *args, **kwargs):
        user = request.user
        post = App.objects.get(order_id=order_id)
        qs = json.dumps(list(App.objects.values()) ,default=str)
        color = random.choices(discover_randow_colors, k=1)

        context = {
            'post': post,
            'color':color,
        }

        return render(request, 'Content/Detail/post_detail.html', context)
