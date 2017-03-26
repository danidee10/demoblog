from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.PostListView.as_view(), name='list_view'),
    url(r'^comments/new/$', views.NewComment.as_view(), name='comments_new'),
    url(r'^post/(?P<slug>[-\w]+)/$', views.PostDetailView.as_view(), name='detail_view')
]