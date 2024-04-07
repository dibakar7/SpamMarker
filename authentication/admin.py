from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User_Information
# Register your models here.
class User_Information_Admin(UserAdmin):
    list_display = ('id', 'name', 'phone_number', 'email')
    ordering = ['id']

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(User_Information, User_Information_Admin)

