# Generated by Django 5.0.7 on 2024-08-15 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_alter_member_number_of_interns_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]
