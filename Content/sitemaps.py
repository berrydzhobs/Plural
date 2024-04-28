from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import App


class AppSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0
    limit = 100

    def items(self):
        return App.objects.all()

    def location(self, obj):
        return reverse("app_detail", args=[obj.order_id])

    def lastmod(self, obj):
        return obj.last_updated