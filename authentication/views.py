import jwt
from .serializers import UserRegisterSerializer, UserLoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from django.core.exceptions import ValidationError
from .models import User_Information
from django.conf import settings

class UserRegisterView(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        input_data = request.data
        serializer = UserRegisterSerializer(data=input_data)
        if serializer.is_valid(raise_exception=True):
            new_user = serializer.register_new_user(input_data)
            if new_user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
class UserLoginView(APIView):
    permission_classes=(permissions.AllowAny,)
    def post(self, request):
        input_data = request.data
        phone_number = input_data['phone_number']
        password = input_data['password']
        serializer = UserLoginSerializer(data=input_data)
        if serializer.is_valid(raise_exception=True):
            user = User_Information.objects.filter(phone_number=phone_number).first()
            if not user:
                raise ValidationError("User not found")
            if not user.check_password(password):
                raise ValidationError("Password is incorrect")
            
            payload = {
                'id': user.id,
            }
            secret_key = settings.SECRET_KEY             
            token = jwt.encode(payload, secret_key, algorithm='HS256')
            response = Response()

            response.set_cookie(key='jwt', value=token, httponly=True)
            return response

class UserLogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data={
            'message':'Successfully Logged Out'
        }
        return response
        
        
	    
