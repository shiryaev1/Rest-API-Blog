from django.urls import path

from posts.views import (
    PostListAPIView,
    PostDetailAPIView,
    PostUpdateAPIView,
    PostDeleteAPIView,
    PostCreateAPIView
)

urlpatterns = [
    path('posts/', PostListAPIView.as_view(), name='list'),
    path('posts/create', PostCreateAPIView.as_view(), name='create'),
    path('posts/<slug>', PostDetailAPIView.as_view(), name='detail'),
    path('posts/<slug>/edit', PostUpdateAPIView.as_view(), name='update'),
    path('posts/<slug>/delete', PostDeleteAPIView.as_view(), name='delete')
]