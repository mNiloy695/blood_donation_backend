# Generated by Django 5.1.5 on 2025-02-16 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0044_alter_donationrequestmodel_blood_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationrequestmodel',
            name='blood',
            field=models.CharField(choices=[('B-', 'B-'), ('AB-', 'AB-'), ('B+', 'B+'), ('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('A-', 'A-'), ('AB+', 'AB+')], max_length=3),
        ),
    ]
