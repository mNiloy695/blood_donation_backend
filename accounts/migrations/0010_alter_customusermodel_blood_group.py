# Generated by Django 5.1.5 on 2025-02-10 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_customusermodel_blood_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='blood_group',
            field=models.CharField(choices=[('B-', 'B-'), ('AB+', 'AB+'), ('A+', 'A+'), ('B+', 'B+'), ('O+', 'O+'), ('O-', 'O-'), ('AB-', 'AB-'), ('A-', 'A-')], max_length=3),
        ),
    ]
