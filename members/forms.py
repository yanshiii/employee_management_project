# forms.py

from django import forms
from .models import Intern

class InternForm(forms.ModelForm):
    class Meta:
        model = Intern
        fields = ['name', 'date_of_joining', 'duration_of_training', 'parent_institution', 'phone_number']

class PasswordResetForm(forms.Form):
    employee_id = forms.CharField(max_length=4)
    old_password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)
