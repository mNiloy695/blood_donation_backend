# Generated by Django 5.1.5 on 2025-02-16 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0042_alter_donationrequestmodel_blood_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donationrequestmodel',
            name='specific_request_model',
        ),
        migrations.AlterField(
            model_name='donationrequestmodel',
            name='blood',
            field=models.CharField(choices=[('AB-', 'AB-'), ('B+', 'B+'), ('AB+', 'AB+'), ('B-', 'B-'), ('O+', 'O+'), ('A+', 'A+'), ('A-', 'A-'), ('O-', 'O-')], max_length=3),
        ),
        migrations.AlterField(
            model_name='donationrequestmodel',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Cancelled', 'Cancelled'), ('Rejected', 'Rejected'), ('Accepted', 'Accepted')], default='Pending', max_length=10),
        ),
    ]
