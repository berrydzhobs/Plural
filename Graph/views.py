from django.shortcuts import render, HttpResponse,redirect, get_object_or_404
from django.contrib.auth.models import User
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

from django.db.models import Q
# Create your views here.
