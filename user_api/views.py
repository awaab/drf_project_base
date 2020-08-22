from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializers import *
from .models import CustomUser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from  django.core.exceptions import ObjectDoesNotExist

class RegisterUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (AllowAny,)

class ActivateUserView(APIView):
    def post(self, request, format=None):
        token = request.data.get("token")
        if token:
            try:
                matching_token = Token.objects.get(key=token)
                user = matching_token.user
            except ObjectDoesNotExist:
                error_msg = {'success': False, "message": "Invalid token"}    
                return Response(error_msg, status=400)
            user.is_confirmed = True
            user.save()
            matching_token.delete()
            return Response({'success': True})
        error_msg = {'success': False, "message": "token field cannot be left blank."}    
        return Response(error_msg, status=400)

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