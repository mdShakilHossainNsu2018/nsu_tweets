from .views import TweetApiView, LikeApiView
from django.urls import path

urlpatterns = [
    path('tweets/', TweetApiView.as_view()),
    path('tweets/likes/', LikeApiView.as_view()),
]
