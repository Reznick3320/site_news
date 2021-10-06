from django.db import models
from django.urls import reverse


# Create your models here.


class NewCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=64, verbose_name='Имя')
    last_name = models.CharField(max_length=64, verbose_name='Фамилия')
    description = models.TextField(blank=True, verbose_name='Описание')
    short_descr = models.CharField(max_length=100, blank=True, verbose_name='Краткое описание')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    image = models.ImageField(upload_to='author_images', blank=True, verbose_name='Фотография')

    class Meta:
        verbose_name_plural = 'Авторы'
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class New(models.Model):
    header = models.CharField(max_length=64, verbose_name='Заголовок')
    image = models.ImageField(upload_to='news_images', blank=True, verbose_name='Фотография')
    description = models.TextField(blank=True, verbose_name='Описание')
    short_descr = models.CharField(max_length=64, blank=True, verbose_name='Краткое описание')
    category = models.ForeignKey(NewCategory, on_delete=models.CASCADE, verbose_name='Категория')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    author = models.ManyToManyField(Author, blank=True, verbose_name='Автор')

    class Meta:
        verbose_name_plural = 'Новости'
        ordering = ['id']

    def __str__(self):
        return f'{self.header} | {self.category.name}'
