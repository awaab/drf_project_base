from .models import CustomUser
from rest_framework import serializers



class BasicCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name']
        

class CustomUserSerializer(BasicCustomUserSerializer):
    class Meta(BasicCustomUserSerializer.Meta):
        fields = ['id', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {
            'password':{'write_only':True},
            'last_name':{'required':False},
            'first_name':{'required':False},
            }
