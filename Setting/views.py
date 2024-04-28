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
from django.contrib.auth import authenticate
from .forms import DeleteAccountForm, UpdateAccountForm, ChangeEmailForm, UpdateProfileForm
from django.core.mail import send_mail
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

import uuid

def generate_verification_token():
    return str(uuid.uuid4())

def verify_token(token):
    # Check if the token is valid
    if token == 'valid-token':
        return True
    else:
        return False

@login_required
#Getting start
#=========================================================
def settings(request,*args,**kwargs):
    return render(request,"Setting/start.html")


def delete_account(request):
    if request.method == 'POST':
        form = DeleteAccountForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=request.user, password=form.cleaned_data['password'])
            if user is not None:
                user.delete()
                return redirect('/')
            else:
                form.add_error(None, 'Invalid password')
    else:
        form = DeleteAccountForm()
    return render(request, 'Setting/delete_account.html', {'form': form})

def update_account(request):
    if request.method == 'POST':
        form = UpdateAccountForm(request.POST)
        if form.is_valid():
            User.objects.filter(username=request.user).update(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                email=form.cleaned_data['email'],
            )
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        form = UpdateAccountForm(initial={
            'username': request.user.username,
            'first_name': request.user.first_name,
            'email': request.user.email,
        })
    return render(request, 'Setting/update_account.html', {'form': form})

def change_email(request):
    if request.method == 'POST':
        form = ChangeEmailForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=request.user, password=form.cleaned_data['password'])
            if user is not None:
                # Generate a verification token and send an email to the new email address
                token = generate_verification_token()
                send_mail(
                    'Verify Your Email Address',
                    'Please click the following link to verify your new email address: '
                    'http://example.com/verify-email?token={}'.format(token),
                    'from@example.com',
                    [form.cleaned_data['new_email']],
                    fail_silently=False,
                )
                return redirect('email_verification_sent')
            else:
                form.add_error(None, 'Invalid password')
    else:
        form = ChangeEmailForm()
    return render(request, 'Setting/change_email.html', {'form': form})

def verify_email(request):
    token = request.GET.get('token')
    if token is None:
        return redirect('invalid_verification_link')
    if verify_token(token):
        User.objects.filter(username=request.user).update(email=new_email)
        return redirect('email_verified')
    else:
        return redirect('invalid_verification_link')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'Setting/change_password.html', {'form': form})

def update_profile(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UpdateProfileForm()
    return render(request, 'Setting/update_profile.html', {'form': form})