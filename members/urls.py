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
    path('details/', views.employee_details, name='emp_details'),

]