# Generated by Django 5.1.5 on 2025-02-15 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestForBlood', '0028_alter_requestforbloodmodel_blood_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestforbloodmodel',
            name='blood',
            field=models.CharField(choices=[('AB+', 'AB+'), ('B-', 'B-'), ('A+', 'A+'), ('AB-', 'AB-'), ('B+', 'B+'), ('A-', 'A-'), ('O+', 'O+'), ('O-', 'O-')], max_length=3),
        ),
        migrations.AlterField(
            model_name='requestforbloodmodel',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Cancelled', 'Cancelled'), ('Rejected', 'Rejected'), ('Accepted', 'Accepted')], default='Pending', max_length=10),
        ),
    ]
