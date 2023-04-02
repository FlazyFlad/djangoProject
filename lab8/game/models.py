from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _

import datetime
import os

# Create your models here.

def rename_file(path, filename):
    name = filename.split('.')[-1]
    if path.news_id is None:
        newsid = News.objects.all().last().news_id + 1
        filename = "%s_%s-%s.%s" % (newsid, 'image', path.category_id, name)
    else:
        filename = "%s_%s-%s.%s" % (path.news_id, 'image', path.category_id, name)


    return os.path.join("images/", filename)
class User(AbstractBaseUser):
    REQUIRED_FIELDS = ('username', 'password', 'email')

    username_validator = UnicodeUsernameValidator()

    user_id = models.AutoField(primary_key=True)
    username = models.CharField(
        _("username"),
        max_length=255,
        unique=True,
        validators=[username_validator],
    )
    password = models.CharField(_("password"), max_length=255)
    email = models.EmailField(_("email"), max_length=255)
    is_superuser = models.BooleanField(_("Superuser"), default=False)
    is_author = models.BooleanField(_("Author"),default=False)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    desciption = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
        ordering = ['category_id']

class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class News(models.Model):
    news_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name="Тема новости")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Текст новости")
    image = models.ImageField(upload_to=rename_file, verbose_name="Изображение")
    time_create = models.DateTimeField(auto_now_add=True);
    time_update = models.DateTimeField(auto_now=True);
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, verbose_name="Жанр")
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, verbose_name="Автор")

    def __str__(self):
        return self.title

    def get_create_time(self):
        return format(self.time_create.strftime('%b %d, %Y'))

    def get_update_time(self):
        return format(self.time_update.strftime('%b %d, %Y'))


    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"
        ordering = ['news_id']

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    content = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)