# Generated by Django 5.1.5 on 2025-02-15 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0031_alter_donationrequestmodel_blood_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='donationrequestmodel',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='donationrequestmodel',
            name='blood',
            field=models.CharField(choices=[('A+', 'A+'), ('AB+', 'AB+'), ('O-', 'O-'), ('AB-', 'AB-'), ('B-', 'B-'), ('A-', 'A-'), ('O+', 'O+'), ('B+', 'B+')], max_length=3),
        ),
        migrations.AlterField(
            model_name='donationrequestmodel',
            name='status',
            field=models.CharField(choices=[('Cancelled', 'Cancelled'), ('Rejected', 'Rejected'), ('Pending', 'Pending'), ('Accepted', 'Accepted')], default='Pending', max_length=10),
        ),
    ]
