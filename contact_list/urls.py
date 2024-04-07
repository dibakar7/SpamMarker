from django.urls import path
from .views import Global_DatabaseView, Individual_ContactListView

urlpatterns = [
    path('profile/', Individual_ContactListView.as_view(), name="profile"),
    path('global-database/', Global_DatabaseView.as_view(), name="global-database"),
]