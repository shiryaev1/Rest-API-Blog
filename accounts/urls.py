from django.urls import path

from accounts.views import (
    UserCreateAPIView,
    )

app_name = 'accounts-api'

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
]