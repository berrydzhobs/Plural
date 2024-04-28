from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from PIL import Image
from Content.models import Topic
from .pro_cat import *
from .namingr import *

# Random order_id
import uuid
import random
import string
from django.db.models.signals import pre_save
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    order_id= models.CharField(max_length=120, unique=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to=get_profile_picture_path, default = "default/user/avatar/avatar.png", blank = True)
    cover = models.ImageField(upload_to=get_profile_cover_path, default = "default/user/cover/cover.png", blank = True)
    trademark = models.ImageField(upload_to=get_profile_trademark_path, blank = True)
    category = models.CharField(max_length=100, choices=ProfileCategory_list, blank = True)
    biography = models.TextField(max_length=500, blank = True)
    birthdate = models.DateField(null=True, blank=True)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    A_T = [
        ('P', 'Personal'),
        ('B', 'Business'),
    ]
    account_type = models.CharField(max_length=1, choices=A_T, null=True, blank=True)
    PRIVACY_CHOICES = [
        ('PUBLIC', 'Public'),
        ('PRIVATE', 'Private'),
    ]
    privacy = models.CharField(max_length=10, choices=PRIVACY_CHOICES, default='PUBLIC')
    root = models.BooleanField(default=False)
    url = models.URLField(max_length=250,blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()

    def get_absolute_url(self):
        return reverse('profile', kwargs={'username': self.user.username})

@receiver(pre_save, sender=Profile)
def set_post_like_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = str(uuid.uuid4())


class ProfileFollow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')
        verbose_name = "Profile Follower"
        verbose_name_plural = "Profile Followers"

    def __str__(self):
        return f'{self.follower} follows {self.following}'



class ProfileFollowRequest(models.Model):
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follow_requests_sent')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='follow_request_received')
    status = models.CharField(max_length=10, choices=[('PENDING', 'Pending'), ('ACCEPTED', 'Accepted'), ('REJECTED', 'Rejected')], default='PENDING')
    request_date = models.DateTimeField(auto_now_add=True)

    def accept(self):
        self.status = 'ACCEPTED'
        self.save()

    def reject(self):
        self.status = 'REJECTED'
        self.save()

    def __str__(self):
        return f'{self.requester.username} request to follow {self.user.username}'


class ProfileInterest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    general = models.ManyToManyField(Topic, related_name='general_interests', blank=True)
    publishing = models.ManyToManyField(Topic, related_name='publishing_interests', blank=True)
    GENDER_CHOICESX = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender= models.CharField(max_length=1, choices=GENDER_CHOICESX, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} :: Interests'

@receiver(post_save, sender=User)
def create_user_interest(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        ProfileInterest.objects.create(user=user)