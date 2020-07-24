from .views import TweetApiView, LikeApiView
from django.urls import path

urlpatterns = [
    path('', TweetApiView.as_view()),
    path('likes/', LikeApiView.as_view()),
]
