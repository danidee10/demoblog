"""Serializers for the API."""

from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """Post serializer."""

    class Meta:
        model = Post
        depth = 1 # display category names instead of id
        fields = (
            'title', 'slug', 'excerpt', 'body', 'categories', 'create_date',
            'comments'
            )
