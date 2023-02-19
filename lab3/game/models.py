from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)




class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    desciption = models.TextField(blank=True)

class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class News(models.Model):
    news_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/")
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    content = models.TextField(blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    news_id = models.ForeignKey(News, on_delete=models.CASCADE)