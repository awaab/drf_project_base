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
    def create(self, validated_data):
        password = validated_data["password"]
        del validated_data["password"]
        user_instance = self.Meta.model(**validated_data)
        user_instance.set_password(password)
        user_instance.save()
        send_activation_email(user_instance)
        return user_instance

class PasswordChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['password']
