from django.conf.urls import url, include
from . import views
from .api_urls import router

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='list_view'),
    url(r'^comments/new/$', views.NewComment.as_view(), name='comments_new'),
    url(r'^post/(?P<slug>[-\w]+)/$', views.PostDetailView.as_view(), name='detail_view'),

    # register api endpoint
    url(r'^api/', include(router.urls))
]