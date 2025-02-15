# Generated by Django 5.1.5 on 2025-02-15 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestForBlood', '0029_alter_requestforbloodmodel_blood_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestforbloodmodel',
            name='blood',
            field=models.CharField(choices=[('AB-', 'AB-'), ('B+', 'B+'), ('A+', 'A+'), ('AB+', 'AB+'), ('B-', 'B-'), ('O-', 'O-'), ('O+', 'O+'), ('A-', 'A-')], max_length=3),
        ),
        migrations.AlterField(
            model_name='requestforbloodmodel',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Rejected', 'Rejected'), ('Pending', 'Pending'), ('Cancelled', 'Cancelled')], default='Pending', max_length=10),
        ),
    ]
