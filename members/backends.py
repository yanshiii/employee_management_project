# members/backends.py
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import Member
import logging
logger = logging.getLogger(__name__)
# pbkdf2_sha256$260000$KmC7czSvcp6u$BRCX2XGnSiyWxKx6VEMAE/FUocXppkAfV0lLKjRyKh8=

class EmployeeIDBackend(BaseBackend):
    def authenticate(self, request, employee_id=None, password=None, **kwargs):
        try:
            member = Member.objects.get(employee_id=employee_id)
            if member and check_password(password, member.password):
                return member
            else:
                logger.info(f"Failed login attempt for employee_id: {employee_id}")
        except Member.DoesNotExist:
            logger.info(f"Member with employee_id: {employee_id} does not exist")
        return None


    def get_user(self, user_id):
        try:
            return Member.objects.get(pk=user_id)
        except Member.DoesNotExist:
            return None