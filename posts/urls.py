from django.urls import path, re_path
from django.contrib import admin

from posts.views import (
    PostListAPIView,
    PostDetailAPIView,
    PostUpdateAPIView,
    PostDeleteAPIView
    )

urlpatterns = [
    path('posts/', PostListAPIView.as_view(), name='list'),
    path('posts/<slug>', PostDetailAPIView.as_view(), name='detail'),
    path('posts/<slug>/edit', PostUpdateAPIView.as_view(), name='update'),
    path('posts/<slug>/delete', PostDeleteAPIView.as_view(), name='delete')
]