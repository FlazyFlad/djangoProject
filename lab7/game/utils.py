from .models import *
from django.db.models import Count

menu = [{'title': "About", 'url_name': 'about'},
        {'title': 'Add News', 'url_name': 'add_post'},
        {'title': 'FeedBack', 'url_name': 'contact'},
        {'title': 'Log In', 'url_name': 'login'},
]


class DataMixin:
    paginate_by = 3
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        user_menu = menu.copy()
        recomends=News.objects.annotate(count=Count('comment')).order_by('-count')[0:3]
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu
        context['cats'] = cats
        context['recomends'] = recomends
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context