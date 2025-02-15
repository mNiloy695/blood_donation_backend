# Generated by Django 5.1.5 on 2025-01-25 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestForBlood', '0007_alter_requestforbloodmodel_blood_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestforbloodmodel',
            name='blood',
            field=models.CharField(choices=[('B+', 'B+'), ('O-', 'O-'), ('O+', 'O+'), ('AB-', 'AB-'), ('A+', 'A+'), ('B-', 'B-'), ('A-', 'A-'), ('AB+', 'AB+')], max_length=3),
        ),
        migrations.AlterField(
            model_name='requestforbloodmodel',
            name='status',
            field=models.CharField(choices=[('Cancelled', 'Cancelled'), ('Rejected', 'Rejected'), ('Accepted', 'Accepted'), ('Pending', 'Pending')], default='Pending', max_length=10),
        ),
    ]
