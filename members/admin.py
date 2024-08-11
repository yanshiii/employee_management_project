from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Member

class MemberAdmin(UserAdmin):
    model = Member
    ordering = ['employee_id']
    
    # Display fields in the list view
    list_display = (
        'employee_id', 'name',  'intercom_off', 'intercom_res','phone_number','department', 'designation',
        'email','pprs_published',
        'number_of_interns',
        'is_staff', 'is_active'
    )
    
    # Fields for editing existing members
    fieldsets = (
        (None, {'fields': ('employee_id', 'password')}),
        ('Personal info', {'fields': (
            'name', 'email', 'phone_number', 'department', 'designation',
            'intercom_off', 'intercom_res', 'pprs_published', 'number_of_interns'
        )}),
        ('Permissions', {'fields': (
            'is_active', 'is_staff', 'is_superuser', 'user_permissions', 'groups'
        )}),
        ('Important dates', {'fields': ('last_login', )}),
    )
    
    # Fields for adding new members
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'employee_id', 'name', 'email', 'password1', 'password2',
                'is_staff', 'is_active', 'intercom_off', 'intercom_res',
                'pprs_published', 'number_of_interns'
            ),
        }),
    )

admin.site.register(Member, MemberAdmin)
