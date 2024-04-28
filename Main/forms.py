from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from Profile.models import Profile

# def ForbiddenUsers(value):
#   forbidden_users = ['admin', 'css', 'js', 'authenticate', 'login', 'logout', 'administrator', 'root',
#   'email', 'user', 'join', 'sql', 'static', 'python', 'delete', 'example', 'test', 'testuser', 'html', 'xxx', 'fuck', 'ass', 'hate']
#   if value.lower() in forbidden_users:
#     raise ValidationError('Invalid name for user, this is a reserverd word.')

# def InvalidUser(value):
#   if '@' in value or '+' in value or '-' in value or '()' in value or '#' in value or '*' in value or '&' in value:
#     raise ValidationError('This is an Invalid username, Do not use these chars: @ , - , + , *, & ')

# def UniqueEmail(value):
#   if User.objects.filter(email__iexact=value).exists():
#     raise ValidationError('User with this email already exists.')

# def UniqueUser(value):
#   if User.objects.filter(username__iexact=value).exists():
#     raise ValidationError('User with this username already exists.')

