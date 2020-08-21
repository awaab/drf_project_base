
from .views import RegisterUserView, UserList
from django.urls import path

urlpatterns = [
    path('register/', RegisterUserView.as_view()),
    path('users/', UserList.as_view()),
]