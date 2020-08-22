
from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='user')

urlpatterns = [
    path('register/', RegisterUserView.as_view()),
    path('change-password/', ChangePasswordView.as_view()),
    path('activate/', ActivateUserView.as_view()),
    path('', include(router.urls)),
]