from django.contrib import admin
from .models import Profile, ProfileInterest, ProfileFollow, ProfileFollowRequest
# Register your models here.
admin.site.register(Profile)
admin.site.register(ProfileFollow)
admin.site.register(ProfileFollowRequest)
admin.site.register(ProfileInterest)