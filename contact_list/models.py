from django.db import models
from authentication.models import User_Information
from phonenumber_field.modelfields import PhoneNumberField


class Contact_List(models.Model):
    parent_user = models.ForeignKey(User_Information, related_name='contact_list', on_delete=models.DO_NOTHING)
    phone_number = PhoneNumberField(blank=False)
    is_spam = models.BooleanField(default=False)
    name = models.CharField(max_length=45, blank=True)

    def __str__(self):
        return self.name
