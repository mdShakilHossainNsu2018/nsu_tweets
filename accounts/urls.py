from .views import UserListApiView, UserDetailApiView, UserCreateAPIView
from django.urls import path

urlpatterns = [
    path('', UserListApiView.as_view()),
    path('<int:pk>/', UserDetailApiView.as_view()),
    path('register/', UserCreateAPIView.as_view()),
]
