# # Create your views here.

# from django.template import loader
# from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
# from .models import Member 
# from django.contrib.auth import authenticate, login
# from django.http import HttpResponse
# from django.contrib.auth.hashers import check_password
# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Intern
# from .forms import InternForm
# from .forms import PasswordResetForm

# def members(request):
#     mymembers = Member.objects.all().values(
#         'name', 'intercom_off', 'intercom_res', 'phone_number', 'department', 
#         'designation', 'email', 'pprs_published', 'number_of_interns'
#     )
#     template = loader.get_template('all_members.html')
#     context = {'mymembers': mymembers}
#     return HttpResponse(template.render(context,request))
    

# # def details(request, name):
# #     mymembers = Member.objects.get(name=name)
# #     template = loader.get_template('details.html')
# #     context = {'mymember': mymembers}
# #     return HttpResponse(template.render(context, request))

# def details(request, name):
#     mymember = Member.objects.get(name=name)
#     interns = mymember.interns.all()  # Fetch all related interns
#     template = loader.get_template('details.html')
#     context = {
#         'mymember': mymember,
#         'interns': interns
#     }
#     return HttpResponse(template.render(context, request))


# def main(request):
#     template = loader.get_template('main.html')
#     return HttpResponse(template.render())


# def divisions(request):
#     template = loader.get_template('all_divisions.html')
#     return HttpResponse(template.render())

# def divmembers(request, department_name):
#     mydata = Member.objects.filter(department=department_name.replace('-', ' '))
#     template = loader.get_template('divmembers.html')
#     context = {
#         'mymembers': mydata,
#         'department_name': department_name.replace('-', ' ')
#     }
#     return HttpResponse(template.render(context, request))

# def print(request):
#     mymembers = Member.objects.all().values()
#     template = loader.get_template('print_members.html')
#     context = {'mymembers': mymembers}
#     return HttpResponse(template.render(context, request))

# def login_view(request):
#     if request.method == "POST":
#         employee_id = request.POST.get('employee_id').strip()
#         password = request.POST.get('password').strip()

#         if not employee_id or not password:
#             return render(request, 'login.html', {'error': 'Please enter both employee ID and password.'})

#         member = authenticate(request, employee_id=employee_id, password=password)
        
#         if member is not None:
#             login(request, member)
#             return redirect('emp_details', employee_id=member.id)  # Pass employee_id
#         else:
#             return render(request, 'login.html', {'error': 'Invalid login credentials'})
#     else:
#         return render(request, 'login.html')

# @login_required
# def employee_details(request, employee_id):
#     member = get_object_or_404(Member, id=employee_id)
#     if request.method == 'POST':
#         # Update member details here
#         member.intercom_off = request.POST.get('intercom_off')
#         member.intercom_res = request.POST.get('intercom_res')
#         member.phone_number = request.POST.get('phone_number')
#         member.department = request.POST.get('department')
#         member.designation = request.POST.get('designation')
#         member.email = request.POST.get('email')
#         member.pprs_published = request.POST.get('pprs_published')
#         member.number_of_interns = request.POST.get('number_of_interns')
        
#         # Validate and save the updated data
#         member.save()

#         # Redirect to the same page after saving to prevent re-submission
#         return redirect('emp_details', employee_id=member.id)  # Pass employee_id

#     return render(request, 'employee_details.html', {'member': member})

# def create_intern(request, member_id):
#     member = get_object_or_404(Member, id=member_id)
#     if request.method == 'POST':
#         form = InternForm(request.POST)
#         if form.is_valid():
#             intern = form.save(commit=False)
#             intern.member = member
#             intern.save()
#             return redirect('details', name=member.name)  # Adjust as needed
#     else:
#         form = InternForm()
    
#     return render(request, 'create_intern.html', {'form': form, 'member': member})

# @login_required
# def password_reset_view(request):
#     if request.method == 'POST':
#         form = PasswordResetForm(request.POST)
#         if form.is_valid():
#             employee_id = form.cleaned_data.get('employee_id')
#             old_password = form.cleaned_data.get('old_password')
#             new_password = form.cleaned_data.get('new_password')
            
#             employee = Member.objects.get(employee_id=employee_id)
#             if employee.check_password(old_password):
#                 employee.set_password(new_password)
#                 employee.save()
#                 return redirect('login')  # Redirect to login page after successful reset
#             else:
#                 form.add_error('old_password', 'Old password is incorrect')
#     else:
#         form = PasswordResetForm()
#     return render(request, 'password_reset.html', {'form': form})

from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Member
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect, get_object_or_404
from .models import Intern
from .forms import InternForm, PasswordResetForm

def members(request):
    mymembers = Member.objects.all().values(
        'name','employee_id', 'intercom_off', 'intercom_res', 'phone_number', 'department', 
        'designation', 'email', 'jpub','cpub','bpub', 'number_of_interns', 'conferences_attended'
    )
    template = loader.get_template('all_members.html')
    context = {'mymembers': mymembers}
    return HttpResponse(template.render(context,request))

def details(request, name):
    mymember = Member.objects.get(name=name)
    interns = mymember.interns.all()  # Fetch all related interns
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
        'interns': interns
    }
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

def login_view(request):
    if request.method == "POST":
        employee_id = request.POST.get('employee_id').strip()
        password = request.POST.get('password').strip()

        if not employee_id or not password:
            return render(request, 'login.html', {'error': 'Please enter both employee ID and password.'})

        member = authenticate(request, employee_id=employee_id, password=password)
        
        if member is not None:
            login(request, member)
            return redirect('emp_details', employee_id=member.id)  # Pass employee_id
        else:
            error_message = "Invalid login credentials. Please check your employee ID and password."
            return render(request, 'login.html', {'error': 'Invalid login credentials'})
    else:
        return render(request, 'login.html')


@login_required
def employee_details(request, employee_id):
    member = get_object_or_404(Member, id=employee_id)
    if request.method == 'POST':
        # Update member details here
        member.intercom_off = request.POST.get('intercom_off')
        member.intercom_res = request.POST.get('intercom_res')
        member.phone_number = request.POST.get('phone_number')
        member.department = request.POST.get('department')
        member.designation = request.POST.get('designation')
        member.email = request.POST.get('email')
        member.jpub = request.POST.get('jpub')
        member.cpub = request.POST.get('cpub')
        member.bpub = request.POST.get('bpub')
        member.number_of_interns = request.POST.get('number_of_interns')
        member.conferences_attended = request.POST.get('conferences_attended')
        
        # Validate and save the updated data
        member.save()

        # Redirect to the same page after saving to prevent re-submission
        return redirect('emp_details', employee_id=member.id)  # Pass employee_id

    return render(request, 'employee_details.html', {'member': member})

def create_intern(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    if request.method == 'POST':
        form = InternForm(request.POST)
        if form.is_valid():
            intern = form.save(commit=False)
            intern.member = member
            intern.save()
            return redirect('details', name=member.name)  # Adjust as needed
    else:
        form = InternForm()
    
    return render(request, 'create_intern.html', {'form': form, 'member': member})

@login_required
def password_reset_view(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            employee_id = form.cleaned_data.get('employee_id')
            old_password = form.cleaned_data.get('old_password')
            new_password = form.cleaned_data.get('new_password')
            
            employee = Member.objects.get(employee_id=employee_id)
            if employee.check_password(old_password):
                employee.set_password(new_password)
                employee.save()
                return redirect('login_view')  # Redirect to login page after successful reset
            else:
                form.add_error('old_password', 'Old password is incorrect')
    else:
        form = PasswordResetForm()
    return render(request, 'password_reset.html', {'form': form})
