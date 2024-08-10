# # Create your models here.

# from django.db import models
# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.hashers import make_password


# class Member(models.Model):
#     employee_id = models.PositiveIntegerField(unique=True)
#     name = models.CharField(max_length=255, unique=True)
#     intercom_off = models.CharField(max_length=10, blank=True, null=True)
#     intercom_res = models.CharField(max_length=10, blank=True, null=True)
#     email = models.EmailField(max_length=254, unique=True, blank=True, null=True)
#     phone_number = models.CharField(max_length=10, default='0000000000')
#     department = models.CharField(max_length=50, blank=True, null=True)
#     designation = models.CharField(max_length=50, blank=True, null=True)
#     pprs_published = models.PositiveIntegerField(default=0)
#     number_of_interns = models.PositiveIntegerField(default=0)
#     password = models.CharField(max_length=128, default=make_password("crri@123"))


#     def save(self, *args, **kwargs):
#         if self.password and not self.password.startswith('pbkdf2_sha256'):
#             self.password = make_password(self.password)
#         super().save(*args, **kwargs)
 
    
#     def __str__(self):
#         return self.name

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password

class MemberManager(BaseUserManager):
    def create_user(self, employee_id, password=None, **extra_fields):
        if not employee_id:
            raise ValueError('The Employee ID must be set')
        member = self.model(employee_id=employee_id, **extra_fields)
        member.set_password(password)
        member.save(using=self._db)
        return member

    def create_superuser(self, employee_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(employee_id, password, **extra_fields)

class Member(AbstractBaseUser):
    employee_id = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=255, unique=True)
    intercom_off = models.CharField(max_length=10, blank=True, null=True)
    intercom_res = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(max_length=254, unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=10, default='0000000000')
    department = models.CharField(max_length=50, blank=True, null=True)
    designation = models.CharField(max_length=50, blank=True, null=True)
    pprs_published = models.PositiveIntegerField(default=0)
    number_of_interns = models.PositiveIntegerField(default=0)
    last_login = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'employee_id'
    REQUIRED_FIELDS = []

    objects = MemberManager()

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith('pbkdf2_sha256'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
