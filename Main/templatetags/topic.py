from django import template
from Graph.models import Topic
from django.db.models import Count
import random

register = template.Library()
@register.inclusion_tag('Main/Base/topic.html')
def topic(user):
    request_user = user
    topics = Topic.objects.filter(pinned = True).order_by('-created_at')[0:7]
    return {'topics': topics}