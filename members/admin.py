# from django.contrib import admin
# from members.models import Employee, Member

# # Register your models here.

# class MemberAdmin(admin.ModelAdmin):
#   list_display = ("name","intercom_off","intercom_res", "phone_number", "department","designation","email","pprs_published","number_of_interns",)
  
# admin.site.register(Member, MemberAdmin)

# class EmployeeAdmin(admin.ModelAdmin):
#     # Define the fields to be displayed in the admin panel
#     list_display = ('user', 'employee_id', 'department', 'designation')
#     # Define the fields that can be edited in the admin panel
#     fields = ('user', 'employee_id', 'intercom_off', 'intercom_res', 'email', 'phone_number', 'department', 'designation', 'pprs_published', 'number_of_interns')
#     # Exclude the employee_id field from the admin form if you don't want to edit it directly
#     # exclude = ('employee_id',)

# admin.site.register(Employee, EmployeeAdmin)


from django.contrib import admin
from .models import Member

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = (
        "employee_id",
        "name", 
        "intercom_off", 
        "intercom_res", 
        "phone_number", 
        "department", 
        "designation", 
        "email", 
        "pprs_published", 
        "number_of_interns",
    )

admin.site.register(Member, MemberAdmin)


# # Admin configuration for Employee model
# class EmployeeAdmin(admin.ModelAdmin):
#     # Display fields in the admin panel list view
#     list_display = ('user', 'employee_id', 'department', 'designation')
#     # Fields to be displayed and editable in the admin form
#     fields = ('user', 'employee_id', 'intercom_off', 'intercom_res', 'email', 'phone_number', 'department', 'designation', 'pprs_published', 'number_of_interns')

# admin.site.register(Employee, EmployeeAdmin)
