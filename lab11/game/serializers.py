import os
from uuid import uuid4
from rest_framework import serializers
from .models import *
from django.utils.text import slugify
from django.contrib.auth.models import User


class NewsSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    class Meta:
        model = News
        fields = "__all__"

    def create(self, validated_data):
        image = validated_data.get('image', None)
        if not image:
            raise serializers.ValidationError('Image is required')
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'image' in validated_data and instance.image:
            os.remove(instance.image.path)

            image = validated_data.pop('image', None)
            instance = super().update(instance, validated_data)

            if image:
                filename = str(uuid4()) + '.' + image.name.split('.')[-1]
                instance.image.save(filename, image)

        else:
            validated_data.get('image', instance.image)
        return instance

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


