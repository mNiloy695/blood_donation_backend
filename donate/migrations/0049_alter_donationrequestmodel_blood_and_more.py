# Generated by Django 5.1.5 on 2025-02-17 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0048_alter_donationrequestmodel_blood_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationrequestmodel',
            name='blood',
            field=models.CharField(choices=[('A-', 'A-'), ('B+', 'B+'), ('O+', 'O+'), ('O-', 'O-'), ('AB-', 'AB-'), ('AB+', 'AB+'), ('B-', 'B-'), ('A+', 'A+')], max_length=3),
        ),
        migrations.AlterField(
            model_name='donationrequestmodel',
            name='status',
            field=models.CharField(choices=[('Cancelled', 'Cancelled'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected'), ('Pending', 'Pending')], default='Pending', max_length=10),
        ),
    ]
