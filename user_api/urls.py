
from .views import RegisterUserView, CustomUserViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='user')

urlpatterns = [
    path('register/', RegisterUserView.as_view()),
    path('', include(router.urls)),
]