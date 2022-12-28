from django.views.generic import ListView
from .models import News, MenuCategory


class CategoryListView(ListView):
    model = MenuCategory
    template_name = 'category_list.html'


class PostByCategoryView(ListView):
    context_object_name = 'news'
    template_name = 'news_list.html'

    def get_queryset(self):
        self.category = MenuCategory.objects.get(slug=self.kwargs['slug'])
        queryset = News.objects.filter(category=self.category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.category
        return context
