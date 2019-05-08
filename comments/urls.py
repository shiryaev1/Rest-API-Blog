from django.urls import path

from comments.views import (
    CommentListAPIView,
    CommentDetailAPIView,
    CommentCreateAPIView
    )

app_name = 'comments-api'

urlpatterns = [
    path('', CommentListAPIView.as_view(), name='list'),
    path('create/', CommentCreateAPIView.as_view(), name='create'),
    path('<pk>', CommentDetailAPIView.as_view(), name='detail'),
    # path('posts/<slug>/edit', PostUpdateAPIView.as_view(), name='update'),
    # path('posts/<slug>/delete', PostDeleteAPIView.as_view(), name='delete')
]