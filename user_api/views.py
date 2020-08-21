from django.shortcuts import render
from rest_framework import generics
from .serializers import CustomUserSerializer
from .models import CustomUser
from rest_framework.permissions import AllowAny, IsAuthenticated

class RegisterUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (AllowAny, )

class UserList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer