from .serializers import Global_Database_Serializer, Individual_ContactListSerializer
from rest_framework import generics, permissions, filters, status
from phonenumbers import format_number, parse, PhoneNumberFormat
from rest_framework.response import Response
from .models import Contact_List
from authentication.models import User_Information
from django.core.exceptions import ValidationError
import jwt
from django.conf import settings


class Individual_ContactListView(generics.ListAPIView):
    serializer_class = Individual_ContactListSerializer
    def get_queryset(self):
        request = self.request
        token = request.COOKIES.get('jwt')
        if not token:
            raise ValidationError("Unauthenticated.")
        secret_key = settings.SECRET_KEY
        payload = jwt.decode(token, secret_key, algorithms="HS256")
        user_id = payload['id']
        user = User_Information.objects.filter(id=user_id).first()
        if not user:
            raise ValidationError("User not found.")
        user_phone_number = user.phone_number
        return User_Information.objects.filter(phone_number=user_phone_number)
    
    
class Global_DatabaseView(generics.ListAPIView):
    serializer_class = Global_Database_Serializer
    queryset = Contact_List.objects.all()
    filter_backends = [filters.SearchFilter]         
    search_fields = ['name', 'phone_number']             #search using name or phone number  
    def get_queryset(self):
        request = self.request
        token = request.COOKIES.get('jwt')
        if not token:
            raise ValidationError("Unauthenticated.")
        secret_key = settings.SECRET_KEY
        payload = jwt.decode(token, secret_key, algorithms="HS256")
        user_id = payload['id']
        user = User_Information.objects.filter(id=user_id).first()
        if not user:
            raise ValidationError("User not found.")
        else:
            return Contact_List.objects.all()


    def put(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number')
        phone_number = format_number(parse(phone_number, 'IN'), PhoneNumberFormat.E164)    #to format the input phone number E.164 format
        Contact_List.objects.filter(phone_number=phone_number).update(is_spam=True)
        return Response(status=status.HTTP_202_ACCEPTED)
