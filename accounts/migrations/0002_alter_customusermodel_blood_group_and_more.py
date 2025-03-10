# Generated by Django 5.1.5 on 2025-01-25 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='blood_group',
            field=models.CharField(choices=[('A+', 'A+'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('A-', 'A-'), ('O+', 'O+'), ('B-', 'B-'), ('B+', 'B+'), ('O-', 'O-')], max_length=3),
        ),
        migrations.AlterField(
            model_name='customusermodel',
            name='last_donation_date',
            field=models.DateField(default='2024-01-01'),
        ),
    ]
