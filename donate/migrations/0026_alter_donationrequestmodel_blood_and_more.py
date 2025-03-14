# Generated by Django 5.1.5 on 2025-02-15 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0025_alter_donationrequestmodel_blood_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationrequestmodel',
            name='blood',
            field=models.CharField(choices=[('B-', 'B-'), ('O-', 'O-'), ('A+', 'A+'), ('O+', 'O+'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('A-', 'A-'), ('B+', 'B+')], max_length=3),
        ),
        migrations.AlterField(
            model_name='donationrequestmodel',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Cancelled', 'Cancelled'), ('Rejected', 'Rejected'), ('Accepted', 'Accepted')], default='Pending', max_length=10),
        ),
    ]
