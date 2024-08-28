from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Member, Intern

class InternInline(admin.TabularInline):
    model = Intern
    extra = 1  # How many blank forms for new Interns to display

class MemberAdmin(UserAdmin):
    model = Member
    ordering = ['employee_id']

    # Display fields in the list view
    list_display = (
        'employee_id', 'name',  'intercom_off', 'intercom_res','phone_number','department', 'designation',
        'email','jpub','cpub','bpub',
        'number_of_interns','conferences_attended',
        'is_staff', 'is_active'
    )

    # Fields for editing existing members
    fieldsets = (
        (None, {'fields': ('employee_id', 'password')}),
        ('Personal info', {'fields': (
            'name', 'email', 'phone_number', 'department', 'designation',
            'intercom_off', 'intercom_res',
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
                'employee_id', 'name', 'email', 'phone_number','department', 'designation', 'password1', 'password2',
                'is_staff', 'is_active', 'intercom_off', 'intercom_res',
            ),
        }),
    )

    # Adding InternInline to the MemberAdmin
    inlines = [InternInline]

admin.site.register(Member, MemberAdmin)
admin.site.register(Intern)
