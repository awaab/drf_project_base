from .models import CustomUser
from rest_framework import serializers
from .mail import send_activation_email

class BasicCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name']
        

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {
            'password':{'write_only':True},
            'last_name':{'required':False},
            'first_name':{'required':False},
            }
    def create(self, validate_data):
        user_instance = super(CustomUserSerializer, self).create(validate_data)
        send_activation_email(user_instance)
        return user_instance

class PasswordChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['password']
        extra_kwargs = {'password':{'write_only':True},}
