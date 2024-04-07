from rest_framework import serializers
from django.core.exceptions import ValidationError
from phonenumber_field.serializerfields import PhoneNumberField
from .models import User_Information

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Information
        fields = '__all__'         # As we need all the fields to register, email is optional
    
    #define new create function to register new user
    def register_new_user(self, validated_data):
        name = validated_data['name']
        phone_number = validated_data['phone_number']
        email = validated_data.get('email')
        password = validated_data['password']

        if email:
            new_user_obj = User_Information.objects.create_user(name=name, phone_number=phone_number, email=email, password=password)
        else:
            new_user_obj = User_Information.objects.create_user(name=name, phone_number=phone_number, password=password)
        new_user_obj.save()
        return new_user_obj

class UserLoginSerializer(serializers.Serializer):
    phone_number = PhoneNumberField()
    password = serializers.CharField()