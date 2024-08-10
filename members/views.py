# from django.template import loader
# from django.http import HttpResponse
# from .models import EmployeeEditForm, Member
# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# # from .forms import EmployeeEditForm
# from .models import Employee

# def members(request):
#     mymembers = Member.objects.all().values()
#     template = loader.get_template('all_members.html')
#     context = {
#         'mymembers': mymembers,
#     }
#     return HttpResponse(template.render(context,request))


# def details(request,name):
#     mymembers = Member.objects.get(name=name)
#     template = loader.get_template('details.html')
#     context = {
#         'mymember': mymembers,
#     }
#     return HttpResponse(template.render(context,request))


# def main(request):
#     template = loader.get_template('main.html')
#     return HttpResponse(template.render())


# def testing(request):
#     mydata = Member.objects.values_list('firstname')
#     template = loader.get_template('template.html')
#     context = {'mymembers': mydata,
#                }
#     return HttpResponse(template.render(context, request))

# def divisions(request):
#     template = loader.get_template('all_divisions.html')
#     return HttpResponse(template.render())

# def divmembers(request, department_name):
#     mydata = Member.objects.filter(department=department_name.replace('-', ' '))
#     template = loader.get_template('divmembers.html')
#     context={
#         'mymembers': mydata,
#         'department_name' : department_name.replace('-', ' '),
#     }
#     return HttpResponse(template.render(context,request))

# def print(request):
#     mymembers = Member.objects.all().values()
#     template = loader.get_template('print_members.html')
#     context = {
#         'mymembers': mymembers,
#     }
#     return HttpResponse(template.render(context,request))

# @login_required
# def profile_view(request):
#     employee = request.user.employee  # Get the employee linked to the logged-in user
#     if request.method == 'POST':
#         form = EmployeeEditForm(request.POST, instance=employee)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')  # Redirect to the profile page after saving
#     else:
#         form = EmployeeEditForm(instance=employee)
    
#     return render(request, 'profile.html', {'form': form})

    
# Create your views here.

from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Member  # Only import models from models.py
# from .models import EmployeeEditForm  # Import forms from forms.py
# from django.contrib.auth import authenticate, login
# from .forms import EmployeeLoginForm


# def members(request):
#     mymembers = Member.objects.all().values()[:9]
#     template = loader.get_template('all_members.html')
#     context = {'mymembers': mymembers}
#     return HttpResponse(template.render(context, request))

def members(request):
    mymembers = Member.objects.all().values(
        'name', 'intercom_off', 'intercom_res', 'phone_number', 'department', 
        'designation', 'email', 'pprs_published', 'number_of_interns'
    )
    template = loader.get_template('all_members.html')
    context = {'mymembers': mymembers}
    return HttpResponse(template.render(context,request))
    

def details(request, name):
    mymembers = Member.objects.get(name=name)
    template = loader.get_template('details.html')
    context = {'mymember': mymembers}
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def divisions(request):
    template = loader.get_template('all_divisions.html')
    return HttpResponse(template.render())

def divmembers(request, department_name):
    mydata = Member.objects.filter(department=department_name.replace('-', ' '))
    template = loader.get_template('divmembers.html')
    context = {
        'mymembers': mydata,
        'department_name': department_name.replace('-', ' ')
    }
    return HttpResponse(template.render(context, request))

def print(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('print_members.html')
    context = {'mymembers': mymembers}
    return HttpResponse(template.render(context, request))
