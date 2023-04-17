from rest_framework import serializers
from .models import *
from django.utils.text import slugify
from django.contrib.auth.models import User


class NewsSerializer(serializers.Serializer):
    news_id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    slug = serializers.CharField(read_only=True)
    content = serializers.CharField()
    image = serializers.ImageField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    author_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    def create(self, validated_data):
        validated_data['slug'] = slugify(validated_data['title'])
        validated_data['category_id'] = Category.objects.get(name=validated_data['category_id'])
        validated_data['author_id'] = User.objects.get(username=validated_data['author_id'])

        return News.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.slug = slugify(validated_data.get("title", instance.title))
        instance.image = validated_data.get('image', instance.image)
        instance.time_update = validated_data.get("time_update", instance.time_update)
        instance.category_id = validated_data.get("category_id", instance.category_id)
        instance.author_id = validated_data.get("author_id", instance.author_id)
        instance.save()
        return instance


class CategorySerializer(serializers.Serializer):
    category_id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    slug = serializers.CharField(read_only=True)
    desciption = serializers.CharField(max_length=255)

    def create(self, validated_data):
        validated_data['slug'] = slugify(validated_data['name'])

        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.desciption = validated_data.get('desciption', instance.desciption)
        instance.save()
        return instance


class CommentsSerializer(serializers.ModelSerializer):
    comment_id = serializers.IntegerField(read_only=True)
    content = serializers.CharField()
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    news = serializers.PrimaryKeyRelatedField(queryset=News.objects.all())

    def create(self, validated_data):
        validated_data['user'] = User.objects.get(username=validated_data['user'])
        validated_data['news'] = News.objects.get(title=validated_data['news'])

        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.content = validated_data.get('content', instance.content)
        instance.user = validated_data.get('user', instance.desciption)
        instance.news = validated_data.get('news', instance.desciption)
        instance.save()
        return instance


