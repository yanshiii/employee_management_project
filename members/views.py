# Create your views here.

from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Member 
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect, get_object_or_404

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


def login_view(request):
    if request.method == "POST":
        employee_id = request.POST.get('employee_id').strip()
        password = request.POST.get('password').strip()

        if not employee_id or not password:
            return render(request, 'login.html', {'error': 'Please enter both employee ID and password.'})

        member = authenticate(request, employee_id=employee_id, password=password)
        
        if member is not None:
            login(request, member)
            return redirect('emp_details')
        else:
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
        
        # Validate and save the updated data
        member.save()

        # Redirect to the same page after saving to prevent re-submission
        return redirect('emp_details', member.employee_id)

    return render(request, 'employee_details.html', {'member': member})

        
from django.db import IntegrityError

def save_member(request):
    if request.method == 'POST':
        try:
            # Attempt to create a new member
            member = Member.objects.create(
                employee_id=request.POST['employee_id'],
                name=request.POST['name'],
                intercom_off=request.POST['intercom_off'],
                intercom_res=request.POST['intercom_res'],
                phone_number=request.POST['phone_number'],
                department=request.POST['department'],
                designation=request.POST['designation'],
                email=request.POST['email'],
                pprs_published=request.POST['pprs_published'],
                number_of_interns=request.POST['number_of_interns'],
            )
            member.set_password('crri@123')
            member.save()
            return redirect('emp_details')
        except IntegrityError as e:
            # Handle the IntegrityError exception
            print(f"Integrity Error: {str(e)}")
            return render(request, '404.html', {'error': str(e)})

