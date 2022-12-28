from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=150)
    category = TreeForeignKey('MenuCategory', on_delete=models.PROTECT, related_name='posts', verbose_name='Категория')
    content = models.TextField(verbose_name='Содержание')
    url = models.CharField(max_length=255, verbose_name='Ссылка', blank=True)
    named_url = models.CharField(max_length=255, verbose_name='Название ссылки', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class MenuCategory(MPTTModel):
    title = models.CharField(max_length=50, unique=True, verbose_name='Название')
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children',
                            db_index=True, verbose_name='Родительская категория')
    slug = models.SlugField()

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('news-by-category', args=[str(self.slug)])

    def __str__(self):
        return self.title