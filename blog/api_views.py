"""Views for the api."""
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.published_posts.all()
    serializer_class = PostSerializer
    