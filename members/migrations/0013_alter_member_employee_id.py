# Generated by Django 5.0.7 on 2024-08-10 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0012_alter_member_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='employee_id',
            field=models.PositiveIntegerField(max_length=3, unique=True),
        ),
    ]
