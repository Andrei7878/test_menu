from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import News, MenuCategory


class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(News, NewsAdmin)


class CategoryAdmin(DjangoMpttAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(MenuCategory, CategoryAdmin)
