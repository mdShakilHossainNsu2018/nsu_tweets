from django.contrib.auth import get_user_model
from rest_framework import serializers
from tweets.models import Tweet, ReTweet, Like

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    tweets = serializers.PrimaryKeyRelatedField(many=True, queryset=Tweet.objects.all())
    re_tweets = serializers.PrimaryKeyRelatedField(many=True, queryset=ReTweet.objects.all())
    likes = serializers.PrimaryKeyRelatedField(many=True, queryset=Like.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'tweets', 're_tweets', 'likes']


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']
        write_only_fields = ('password',)
        extra_kwargs = {
            'password': {'write_only': True},
        }
    
    def create(self, validated_data):
        user = User(**validated_data)

        user.set_password(validated_data['password'])
        user.save()
        return user
