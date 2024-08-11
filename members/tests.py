from django.test import TestCase
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_tennis_club.settings')
django.setup()

# from django.contrib.auth.hashers import check_password

# # Now you can use Django's settings and functions
# hashed_password = 'pbkdf2_sha256$720000$1YBPDImKQ1H8tyIlqlYgy9$QfoAJthywto5pk5bdGYhs/8owX8pCXrxtHwuk9OSPpQ='
# password = 'crri@123'

# if check_password(password, hashed_password):
#     print("Password matches!")
# else:
#     print("Password does not match.")


from django.contrib.auth import authenticate

# Test with known employee ID and password
user = authenticate(employee_id='693', password='crri@123')
print(user)  # Should