from rest_framework.generics import ListAPIView, RetrieveAPIView

from posts.models import  Post
from posts.serializers import PostSerializer


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class =