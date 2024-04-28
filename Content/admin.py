from django.contrib import admin

# Register your models here.
from .models import App, AppCarousel

admin.site.register(App)

admin.site.register(AppCarousel)