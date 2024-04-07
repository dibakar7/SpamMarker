from django.urls import path
from .views import UserLoginView, UserRegisterView, UserLogoutView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="registration"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('logout/', UserLogoutView.as_view(), name="logout"),
]
