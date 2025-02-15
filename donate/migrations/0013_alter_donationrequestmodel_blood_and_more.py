# Generated by Django 5.1.5 on 2025-01-25 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0012_alter_donationrequestmodel_blood_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationrequestmodel',
            name='blood',
            field=models.CharField(choices=[('B+', 'B+'), ('O-', 'O-'), ('O+', 'O+'), ('AB+', 'AB+'), ('A-', 'A-'), ('AB-', 'AB-'), ('B-', 'B-'), ('A+', 'A+')], max_length=3),
        ),
        migrations.AlterField(
            model_name='donationrequestmodel',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Rejected', 'Rejected'), ('Accepted', 'Accepted'), ('Cancelled', 'Cancelled')], default='Pending', max_length=10),
        ),
    ]
