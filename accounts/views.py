from django.db.models import Q
from django.contrib.auth import get_user_model


from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
    )
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView
    )

from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
    )

from posts.pagination import PostPageNumberPagination
from posts.permissions import IsOwnerOrReadOnly

User = get_user_model()

from accounts.serializers import (
    UserCreateSerializer
    )


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()