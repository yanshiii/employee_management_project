from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class MemberManager(BaseUserManager):
    def create_user(self, employee_id, password=None, **extra_fields):
        if not employee_id:
            raise ValueError('The Employee ID must be set')
        member = self.model(employee_id=employee_id, **extra_fields)
        member.set_password(password)
        member.save(using=self._db)
        return member

    def create_superuser(self, employee_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)  # Ensure this is set for superusers
        return self.create_user(employee_id, password, **extra_fields)

class Member(AbstractBaseUser, PermissionsMixin):                     
    DEPARTMENT_CHOICES = [('Bridge Engineering and Structures Division', 'Bridge Engineering and Structures Division'),
    ('Geotechnical Engineering Division', 'Geotechnical Engineering Division'),
    ('Flexible Pavements Division', 'Flexible Pavements Division'),
    ('Pavement Evaluation Division', 'Pavement Evaluation Division'),
    ('Rigid Pavements Division', 'Rigid Pavements Division'),
    ('Transportation Planning and Environment Division', 'Transportation Planning and Environment Division'),
    ('Traffic Engineering and Safety Division', 'Traffic Engineering and Safety Division'), ('Knowledge Resource Centre','Knowledge Resource Centre'),
    ('Director Office','Director Office'),
    ('Controller of Administration','Controller of Administration'),
    ('Administration Office','Administration Office'),
    ('Computer Centre and Network Division','Computer Centre and Network Division'),
    ('Information Liaison and Training Division','Information Liaison and Training Division'),
    ('Planning Monitoring and Evaluation Division','Planning Monitoring and Evaluation Division'),
    ('Engineering Services Division','Engineering Services Division' ) ,        
    ('Mechanical and Transport Division' ,'Mechanical and Transport Division' ),
    ('Quality Management Division','Quality Management Division'),
    ('MBSQ Maintenance Division','MBSQ Maintenance Division'),('Establishment Section I','Establishment Section I' ),
    ('Establishment Section II','Establishment Section II'),
    ('Finance and Accounts Section','Finance and Accounts Section') ,
    ('Store and Purchase Section','Store and Purchase Section'),      
    ('Personnel Cell','Personnel Cell'), 
    ('Vigilance Section','Vigilance Section'),
    ('Rajbhasha','Rajbhasha'),
    ('Right to Information Cell','Right to Information Cell' ), 
    ('Canteen','Canteen'),
    ('Guest House','Guest House' ),
    ('Horticulture','Horticulture' ), 
    ('Security Section','Security Section'),]
    
    employee_id = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=255)
    intercom_off = models.CharField(max_length=10)
    intercom_res = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    department = models.CharField(max_length=255, choices=DEPARTMENT_CHOICES)
    designation = models.CharField(max_length=255)
    email = models.EmailField()
    jpub = models.CharField(max_length=255, default='-')
    cpub = models.CharField(max_length=255, default='-')
    bpub = models.CharField(max_length=255, default='-')
    number_of_interns = models.CharField(max_length=255, default='-')
    conferences_attended = models.CharField(max_length=255, default='-')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = MemberManager()

    USERNAME_FIELD = 'employee_id'
    REQUIRED_FIELDS = ['email']  
    def __str__(self):
        return self.employee_id
    
class Intern(models.Model):
    member = models.ForeignKey(Member, related_name='interns', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_of_joining = models.DateField()
    duration_of_training = models.CharField(max_length=100)
    parent_institution = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name
