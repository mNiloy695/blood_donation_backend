# Generated by Django 5.1.5 on 2025-02-10 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_customusermodel_blood_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='blood_group',
            field=models.CharField(choices=[('O+', 'O+'), ('AB-', 'AB-'), ('B+', 'B+'), ('A-', 'A-'), ('A+', 'A+'), ('AB+', 'AB+'), ('O-', 'O-'), ('B-', 'B-')], max_length=3),
        ),
    ]
