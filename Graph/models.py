from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.urls import reverse
# Random order_id
import uuid
import random
import string
from django.db.models.signals import pre_save
from django.db.models.signals import post_save
from django.dispatch import receiver
from .namingr import *
from django.utils.crypto import get_random_string



class Topic(models.Model):
	order_id= models.CharField(max_length=120, unique=True, blank=True)
	name = models.CharField(max_length=150,db_index=True)
	icon = models.CharField(max_length=150,db_index=True, default="mdi mdi-text") 
	thumbnail = models.ImageField(upload_to=get_topic_picture_path, default = "default/topic/thumbnail/default.png",blank=True)
	description = models.TextField(max_length=5000,blank=True)
	color = models.CharField(max_length=150, blank=True , default="#75d317")
	parent = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='+')
	pinned = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	last_updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-created_at']

	@property
	def children(self):
		return Topic.objects.filter(parent=self).order_by('-date')[:0]

	@property
	def children_total(self):
		return Topic.objects.filter(parent=self).order_by('-date')

	@property
	def is_parent(self):
		if self.parent is None:
			return True
		return False

	def __str__(self):
		return self.name

@receiver(pre_save, sender=Topic)
def set_post_like_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = str(uuid.uuid4())