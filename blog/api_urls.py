"""Endpoints for the API URL's."""

from rest_framework import routers
from .api_views import PostViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)