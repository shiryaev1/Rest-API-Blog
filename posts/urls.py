from django.urls import path, re_path
from django.contrib import admin

from .views import (
    PostListAPIView,
    PostDetailAPIView
    )

urlpatterns = [
    path('posts/', PostListAPIView.as_view(), name='list'),
    path('posts/<slug>', PostDetailAPIView.as_view(), name='detail')
]