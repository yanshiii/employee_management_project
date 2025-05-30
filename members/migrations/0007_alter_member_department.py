# Generated by Django 5.0.7 on 2024-08-27 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_rename_pprs_published_member_bpub_member_cpub_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='department',
            field=models.CharField(choices=[('Bridge Engineering and Structures Division', 'Bridge Engineering and Structures Division'), ('Geotechnical Engineering Division', 'Geotechnical Engineering Division'), ('Flexible Pavements Division', 'Flexible Pavements Division'), ('Pavement Evaluation Division', 'Pavement Evaluation Division'), ('Rigid Pavements Division', 'Rigid Pavements Division'), ('Transportation Planning and Environment Division', 'Transportation Planning and Environment Division'), ('Traffic Engineering and Safety Division', 'Traffic Engineering and Safety Division'), ('Knowledge Resource Centre', 'Knowledge Resource Centre'), ('Director Office', 'Director Office'), ('Controller of Administration', 'Controller of Administration'), ('Administration Office', 'Administration Office'), ('Computer Centre and Network Division', 'Computer Centre and Network Division'), ('Information Liaison and Training Division', 'Information Liaison and Training Division'), ('Planning Monitoring and Evaluation Division', 'Planning Monitoring and Evaluation Division'), ('Engineering Services Division', 'Engineering Services Division'), ('Mechanical and Transport Division', 'Mechanical and Transport Division'), ('Quality Management Division', 'Quality Management Division'), ('MBSQ Maintenance Division', 'MBSQ Maintenance Division'), ('Establishment Section I', 'Establishment Section I'), ('Establishment Section II', 'Establishment Section II'), ('Finance and Accounts Section', 'Finance and Accounts Section'), ('Store and Purchase Section', 'Store and Purchase Section'), ('Personnel Cell', 'Personnel Cell'), ('Vigilance Section', 'Vigilance Section'), ('Rajbhasha', 'Rajbhasha'), ('Right to Information Cell', 'Right to Information Cell'), ('Canteen', 'Canteen'), ('Guest House', 'Guest House'), ('Horticulture', 'Horticulture'), ('Security Section', 'Security Section')], max_length=255),
        ),
    ]
