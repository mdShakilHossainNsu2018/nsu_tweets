from .views import TweetApiView
from django.urls import path

urlpatterns = [
    path('tweets/', TweetApiView.as_view()),
]
