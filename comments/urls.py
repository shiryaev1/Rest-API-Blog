from django.urls import path

from comments.views import (
    CommentListAPIView,
    CommentDetailAPIView,
    CommentCreateAPIView
    )

app_name = 'comments-api'

urlpatterns = [
    path('comments/', CommentListAPIView.as_view(), name='list'),
    path('comments/create/', CommentCreateAPIView.as_view(), name='create'),
    path('comments/pk=<pk>', CommentDetailAPIView.as_view(), name='detail'),
    # path('posts/<slug>/edit', PostUpdateAPIView.as_view(), name='update'),
    # path('posts/<slug>/delete', PostDeleteAPIView.as_view(), name='delete')
]