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

from django.contrib.auth.decorators import login_required
from .models import Member 

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password

from django.shortcuts import render, redirect, get_object_or_404


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


# def employee_login(request):
#     if request.method == 'POST':
#         employee_id = request.POST.get('employee_id')
#         password = request.POST.get('password')
#         user = authenticate(request, employee_id=employee_id, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('employee_details')
#         else:
#             return HttpResponse('Invalid login credentials')
#     return render(request, 'login.html')



# def login_view(request):
#     if request.method == "POST":
#         employee_id = request.POST['employee_id']
#         password = request.POST['password']
        
#         # Try to find the member by employee_id
#         try:
#             member = Member.objects.get(employee_id=employee_id)
#             # Validate the password
#             if check_password(password, member.password):
#                 # Password is correct
#                 login(request, member)
#                 return redirect('emp_details', employee_id=member.employee_id)
#             else:
#                 # Password is incorrect
#                 return render(request, 'login.html', {'error': 'Invalid login credentials'})
#         except Member.DoesNotExist:
#             return render(request, 'login.html', {'error': 'Employee ID not found'})
#     else:
#         return render(request, 'login.html')
    


def login_view(request):
    if request.method == "POST":
        employee_id = request.POST.get('employee_id').strip()
        password = request.POST.get('password').strip()

        if not employee_id or not password:
            return render(request, 'login.html', {'error': 'Please enter both employee ID and password.'})
        
        # Authenticate using the custom EmployeeIDBackend
        member = authenticate(request, employee_id=employee_id, password=password)
        # print(f"Authenticated member: {member}")
        
        if member is not None:
            # Login successful
            login(request, member)
            return redirect('emp_details', employee_id=member.employee_id)

        
        else:
            # Authentication failed
            return render(request, 'login.html', {'error': 'Invalid login credentials'})
    else:
        return render(request, 'login.html')



@login_required
def employee_details(request):
    member = request.user
    if request.method == 'POST':
        # Update member details here
        member.intercom_off = request.POST.get('intercom_off')
        member.intercom_res = request.POST.get('intercom_res')
        member.phone_number = request.POST.get('phone_number')
        member.department = request.POST.get('department')
        member.designation = request.POST.get('designation')
        member.email = request.POST.get('email')
        member.pprs_published = request.POST.get('pprs_published')
        member.number_of_interns = request.POST.get('number_of_interns')
        member.save()
        return redirect('emp_details')

    return render(request, 'employee_details.html', {'member': member})
