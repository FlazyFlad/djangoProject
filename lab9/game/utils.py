from .models import *
from django.db.models import Count
from django.core.cache import cache

menu = [{'title': "About", 'url_name': 'about'},
        {'title': 'Add News', 'url_name': 'add_post'},
        {'title': 'FeedBack', 'url_name': 'contact'},
]


class DataMixin:
    paginate_by = 3
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = cache.get('cats')
        if not cats:
            cats = Category.objects.all()[:5]
            cache.set('cats', cats, 60)
        user_menu = menu.copy()
        recomends = cache.get('recomends')
        if not recomends:
            recomends=News.objects.annotate(count=Count('comment')).order_by('-count')[0:3]
            cache.set('recomends', recomends, 10)
        if not self.request.user.is_authenticated:
            user_menu.pop(1)


        context['menu'] = user_menu
        context['cats'] = cats
        context['recomends'] = recomends
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context