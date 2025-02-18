# Generated by Django 5.1.5 on 2025-02-16 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestForBlood', '0035_alter_requestforbloodmodel_blood_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestforbloodmodel',
            name='blood',
            field=models.CharField(choices=[('B-', 'B-'), ('AB+', 'AB+'), ('O+', 'O+'), ('AB-', 'AB-'), ('B+', 'B+'), ('A+', 'A+'), ('O-', 'O-'), ('A-', 'A-')], max_length=3),
        ),
        migrations.AlterField(
            model_name='requestforbloodmodel',
            name='status',
            field=models.CharField(choices=[('Cancelled', 'Cancelled'), ('Rejected', 'Rejected'), ('Pending', 'Pending'), ('Accepted', 'Accepted')], default='Pending', max_length=10),
        ),
    ]
