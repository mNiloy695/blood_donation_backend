# Generated by Django 5.1.5 on 2025-02-16 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestForBlood', '0037_alter_requestforbloodmodel_blood_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestforbloodmodel',
            name='blood',
            field=models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('O+', 'O+'), ('B-', 'B-'), ('AB-', 'AB-'), ('O-', 'O-'), ('AB+', 'AB+'), ('B+', 'B+')], max_length=3),
        ),
        migrations.AlterField(
            model_name='requestforbloodmodel',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Cancelled', 'Cancelled'), ('Rejected', 'Rejected'), ('Pending', 'Pending')], default='Pending', max_length=10),
        ),
    ]
