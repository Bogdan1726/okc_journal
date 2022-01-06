from django.db import models


# Create your models here.

class News(models.Model):
    DoesNotExist = None
    objects = None
    title = models.CharField(max_length=150, verbose_name='Тема')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публікації')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='статус')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='категорія', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'
        ordering = ['-created_at']


class Category(models.Model):
    DoesNotExist = None
    objects = None
    title = models.CharField(max_length=150, db_index=True, verbose_name='Назва категорії')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['title']


