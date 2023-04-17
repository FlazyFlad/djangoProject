from django import template
from game.models import *
from django.db.models import Count

register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.all()

@register.inclusion_tag("game/bites/recomends.html")
def show_recomends():
    recomends = News.objects.annotate(count=Count('comment')).order_by('-count')[0:3]
    return {"recomends": recomends}