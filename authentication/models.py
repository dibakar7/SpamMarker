from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class User_InformationManager(BaseUserManager):
    def create_user(self, name, phone_number, email=None, password=None):
        if not name:
            raise ValueError("User must have an name")
        if not phone_number:
            raise ValueError('Users must have an phone number')
        user = self.model(
            name=name,
            phone_number=phone_number,
        )
        if email:
            user.email = self.normalize_email(email)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, phone_number, email=None, password=None):
        user = self.create_user(
            name,
            phone_number=phone_number,
            password=password,
        )
        if email:
            user.email= self.normalize_email(email)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
class User_Information(AbstractBaseUser):
    name = models.CharField(max_length=45, blank=False)
    phone_number = PhoneNumberField(blank=False, unique=True)
    email = models.EmailField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = User_InformationManager()
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['name', 'password']

    # class Meta:
    #     app_label = 'user_info'
    def __str__(self):
        return self.name
    def has_module_perms(self, app_label):
        return self.is_admin
    def has_perm(self, perm, obj=None):
        return self.is_admin
    