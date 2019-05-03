from django.urls import path
from django.contrib import admin

from .views import PostListAPIView

urlpatterns = [
    path('', PostListAPIView.as_view(), name='list')
]