# Generated by Django 5.1.5 on 2025-02-17 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0041_alter_customusermodel_blood_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='blood_group',
            field=models.CharField(choices=[('AB+', 'AB+'), ('O-', 'O-'), ('B+', 'B+'), ('AB-', 'AB-'), ('A-', 'A-'), ('A+', 'A+'), ('B-', 'B-'), ('O+', 'O+')], max_length=3),
        ),
    ]
