from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Random order_id
import uuid
import random
import string
from django.db.models.signals import pre_save
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class SearchKeyword(models.Model):
    term = models.CharField(max_length=355)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    	return f'{self.term}'