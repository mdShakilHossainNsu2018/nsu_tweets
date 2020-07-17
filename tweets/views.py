from .serializers import TweetSerializer
from rest_framework import generics
from .models import Tweet
from rest_framework import permissions


class TweetApiView(generics.ListCreateAPIView):

    serializer_class = TweetSerializer
    queryset = Tweet.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


