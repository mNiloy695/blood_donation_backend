# Generated by Django 5.1.5 on 2025-02-14 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestForBlood', '0018_alter_requestforbloodmodel_blood_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestforbloodmodel',
            name='blood',
            field=models.CharField(choices=[('A-', 'A-'), ('B-', 'B-'), ('O+', 'O+'), ('B+', 'B+'), ('O-', 'O-'), ('AB-', 'AB-'), ('A+', 'A+'), ('AB+', 'AB+')], max_length=3),
        ),
    ]
