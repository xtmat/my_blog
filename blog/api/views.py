from rest_framework import generics
from blog.api.serializers import PostSerializer
from blog.models import Post
from rest_framework.authentication import SessionAuthentication,TokenAuthentication

class PostList(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication,TokenAuthentication]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
