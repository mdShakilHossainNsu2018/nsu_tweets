from rest_framework import serializers
from .models import Tweet, ReTweet, Like


class TweetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    image = serializers.ImageField(required=False, max_length=None, use_url=True, allow_empty_file=True, allow_null=True)

    class Meta:
        model = Tweet
        fields = ['id', 'owner', 'tweet', 'image', 'created_at', 'updated_at']
        read_only_fields = ['id', 'owner']

        extra_kwargs = {'picture': {'required': False}}


class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = ['id', 'owner', 'likes', 'tweet']
        read_only_fields = ['id', 'owner']
