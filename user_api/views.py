from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializers import *
from .models import CustomUser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

class RegisterUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (AllowAny,)

class CustomUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    def get_serializer_class(self):
        if self.request.user and self.request.user.is_authenticated:
            return CustomUserSerializer
        else:
            return BasicCustomUserSerializer

class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = PasswordChangeSerializer
    model = CustomUser
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.object.set_password(serializer.data.get("password"))
            self.object.save()
            return Response({'success': True})

        return Response(serializer.errors, status=400)