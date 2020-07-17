from rest_framework.exceptions import ValidationError
from .serializers import TweetSerializer, LikeSerializer
from rest_framework import generics
from .models import Tweet, Like
from rest_framework import permissions


class TweetApiView(generics.ListCreateAPIView):
    serializer_class = TweetSerializer
    queryset = Tweet.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeApiView(generics.ListCreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        queryset = Like.objects.filter(owner=self.request.user)
        if queryset.exists():
            queryset.delete()
            raise ValidationError('user already liked so it\'s deleted now...')

        serializer.save(owner=self.request.user)


