# Generated by Django 5.1.5 on 2025-02-16 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestForBlood', '0034_alter_requestforbloodmodel_blood_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestforbloodmodel',
            name='blood',
            field=models.CharField(choices=[('A+', 'A+'), ('AB-', 'AB-'), ('B+', 'B+'), ('A-', 'A-'), ('AB+', 'AB+'), ('O-', 'O-'), ('B-', 'B-'), ('O+', 'O+')], max_length=3),
        ),
        migrations.AlterField(
            model_name='requestforbloodmodel',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Cancelled', 'Cancelled'), ('Rejected', 'Rejected')], default='Pending', max_length=10),
        ),
    ]
