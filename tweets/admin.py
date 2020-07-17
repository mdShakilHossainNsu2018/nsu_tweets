from django.contrib import admin
from .models import Tweet, Like, ReTweet

admin.site.register(Tweet)
admin.site.register(Like)
admin.site.register(ReTweet)
