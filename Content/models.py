from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from Graph.models import Topic
from .namingr import get_app_icon_path, get_app_thumbnail_path, get_appcarousel_media_path
import uuid
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.utils.crypto import get_random_string


class App(models.Model):
    order_id = models.CharField(max_length=120, unique=True, blank=True)
    short_code = models.CharField(max_length=10, unique=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField(max_length=5000, blank=True, null=True)
    icon = models.ImageField(upload_to=get_app_icon_path, max_length=5000, blank=True,
                              default="default/app/icon/icon.png")
    thumbnail = models.ImageField(upload_to=get_app_thumbnail_path, max_length=5000, blank=True,
                                   default="default/app/thumbnail/thumbnail.png")
    url = models.URLField(max_length=250, blank=True)
    color = models.CharField(max_length=150, blank=True, default="#2a6602")
    background_color = models.CharField(max_length=150, blank=True, default="#ccedab")
    category = models.ForeignKey(Topic, related_name="app_category", on_delete=models.SET_NULL, null=True, blank=True)
    views = models.ManyToManyField(User, related_name="app_views", blank=True)
    views_counter = models.IntegerField(default=0)
    pinned = models.BooleanField(default=False)
    edited = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.order_id:
            base_order_id = slugify(self.name)
            self.order_id = f"{base_order_id}-{self.created_at.strftime('%Y-%m-%d-%H-%M-%S')}"
        if not self.short_code:
            self.short_code = get_random_string(length=10)
        super().save(*args, **kwargs)

    def total_views(self):
        return self.views.count()

    def is_popular(self):
        return self.views_counter > 100

    def get_absolute_url(self):
        return reverse('app_detail', kwargs={'order_id': self.order_id})

    def __str__(self):
        return f'{self.user.username}::{self.name}'

    class Meta:
        ordering = ['-created_at']


@receiver(pre_save, sender=App)
def set_post_like_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = str(uuid.uuid4())


class AppCarousel(models.Model):
    app = models.ForeignKey(App, default=None, on_delete=models.CASCADE)
    media = models.ImageField(upload_to=get_appcarousel_media_path, max_length=5000, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.app.name}'
