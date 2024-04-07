from django.contrib import admin
from .models import Contact_List

class Contact_List_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'is_spam')
    ordering = ['id']

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(Contact_List, Contact_List_Admin)
