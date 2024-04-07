from rest_framework import serializers
from .models import Contact_List
from authentication.models import User_Information

# The below code is for serializing data regarding contact list of a logged in user
class Individual_ContactListSerializer(serializers.HyperlinkedModelSerializer):
    contactList = serializers.SerializerMethodField()
    class Meta:
        model = User_Information
        fields = ('id', 'name', 'phone_number', 'email', 'contactList')
    
    def get_contactList(self, object):
        items = object.contact_list.all().values_list('name', 'phone_number', 'is_spam')
        # Convert PhoneNumber objects to strings
        items = [
                    {
                        "name": name,
                        "phone_number": str(phone_number),
                        "is_spam": is_spam
                    }
                    for name, phone_number, is_spam in items
                ] 
        return list(items)

class Global_Database_Serializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField()
    class Meta:
        model = Contact_List
        fields = ('name', 'phone_number','email', 'is_spam')
    
    def get_email(self, obj):
        loggedin_user = self.context['request'].user
        if obj.parent_user == loggedin_user and User_Information.objects.filter(phone_number = obj.phone_number).exists():
            user = User_Information.objects.get(phone_number = obj.phone_number)
            return user.email
        return None
