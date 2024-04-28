from django.urls import reverse
from django.contrib.sitemaps import Sitemap
from Content.models import App


class Startpage(Sitemap):
    changefreq = "yearly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return ['Startqt', 'Career']

    def location(self, item):
        return reverse(item)

    def items(self):
        return ['Startqt']
 
class Appsitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'http'

    def items(self):
        return App.objects.all()

    def lastmod(self, obj):
        return obj.date
        
    def location(self,obj):
        return reverse('app', kwargs={'order_id': obj.order_id})