from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('divisions/', views.divisions, name = 'divisions'),
    path('divisions/<str:department_name>/', views.divmembers, name='divmembers'),
    path('members/details/<str:name>', views.details, name='details'),
    path('print/', views.print, name='print'),
    path('login/', views.login_view, name='login_view'),
    path('details/<int:employee_id>/', views.employee_details, name='emp_details'), 
    path('reset-password/', views.password_reset_view, name='reset_password'),
]