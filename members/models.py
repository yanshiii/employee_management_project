from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

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
        extra_fields.setdefault('is_superuser', True)  # Ensure this is set for superusers
        return self.create_user(employee_id, password, **extra_fields)

class Member(AbstractBaseUser, PermissionsMixin):
    employee_id = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=255)
    intercom_off = models.CharField(max_length=10)
    intercom_res = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    department = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    email = models.EmailField()
    pprs_published = models.CharField(max_length=255)
    number_of_interns = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = MemberManager()

    USERNAME_FIELD = 'employee_id'
    REQUIRED_FIELDS = ['email']  # Add fields required when creating a superuser

    def __str__(self):
        return self.employee_id
