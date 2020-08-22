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
            serializer = CustomUserSerializer(user)
            return Response(serializer)
        error_msg = {'success': False, "message": "token field cannot be left blank."}    
        return Response(error_msg, status=400)

class CustomUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    def get_serializer_class(self):
        user = self.request.user
        if user and user.is_authenticated and user.is_confirmed:
            return CustomUserSerializer
        else:
            return BasicCustomUserSerializer

class ChangePasswordView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        user = request.user
        serializer = PasswordChangeSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.data.get("password"))
            user.save()
            return Response({'success': True})

        return Response(serializer.errors, status=400)