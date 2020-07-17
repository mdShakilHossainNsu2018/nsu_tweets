from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Tweet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tweet


class Like(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey('Tweet', on_delete=models.CASCADE)
    likes = models.BooleanField(default=False)

    def __str__(self):
        return self.owner.username


class ReTweet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    base_tweet = models.ForeignKey('Tweet', on_delete=models.CASCADE)
    tweet = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tweet
