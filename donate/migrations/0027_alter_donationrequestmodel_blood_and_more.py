# Generated by Django 5.1.5 on 2025-02-15 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0026_alter_donationrequestmodel_blood_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationrequestmodel',
            name='blood',
            field=models.CharField(choices=[('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('A-', 'A-'), ('O-', 'O-'), ('O+', 'O+'), ('B-', 'B-')], max_length=3),
        ),
        migrations.AlterField(
            model_name='donationrequestmodel',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected'), ('Cancelled', 'Cancelled')], default='Pending', max_length=10),
        ),
    ]
