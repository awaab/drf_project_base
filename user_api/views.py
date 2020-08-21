from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializers import CustomUserSerializer, BasicCustomUserSerializer
from .models import CustomUser
from rest_framework.permissions import AllowAny, IsAuthenticated

class RegisterUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (AllowAny, )

class CustomUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    def get_serializer_class(self):
        if self.request.user and self.request.user.is_authenticated:
            return CustomUserSerializer
        else:
            return BasicCustomUserSerializer