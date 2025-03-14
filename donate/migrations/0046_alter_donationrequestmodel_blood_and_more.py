# Generated by Django 5.1.5 on 2025-02-17 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0045_alter_donationrequestmodel_blood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationrequestmodel',
            name='blood',
            field=models.CharField(choices=[('O-', 'O-'), ('AB+', 'AB+'), ('A+', 'A+'), ('B+', 'B+'), ('B-', 'B-'), ('AB-', 'AB-'), ('A-', 'A-'), ('O+', 'O+')], max_length=3),
        ),
        migrations.AlterField(
            model_name='donationrequestmodel',
            name='status',
            field=models.CharField(choices=[('Cancelled', 'Cancelled'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected'), ('Pending', 'Pending')], default='Pending', max_length=10),
        ),
    ]
