from rest_framework import serializers
from .models import Tweet, ReTweet, Like


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['id', 'owner', 'tweet', 'image', 'created_at', 'updated_at']
        read_only_fields = ['id', 'owner']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'owner', 'likes', 'tweet']
        read_only_fields = ['id', 'owner']
