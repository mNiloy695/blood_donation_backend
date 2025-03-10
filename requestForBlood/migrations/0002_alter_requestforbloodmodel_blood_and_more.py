# Generated by Django 5.1.5 on 2025-01-18 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestForBlood', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestforbloodmodel',
            name='blood',
            field=models.CharField(choices=[('O+', 'O+'), ('A-', 'A-'), ('O-', 'O-'), ('B+', 'B+'), ('AB+', 'AB+'), ('A+', 'A+'), ('AB-', 'AB-'), ('B-', 'B-')], max_length=3),
        ),
        migrations.AlterField(
            model_name='requestforbloodmodel',
            name='status',
            field=models.CharField(choices=[('Cancelled', 'Cancelled'), ('Rejected', 'Rejected'), ('Pending', 'Pending'), ('Accepted', 'Accepted')], default='Pending', max_length=10),
        ),
    ]
