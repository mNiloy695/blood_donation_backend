# Generated by Django 5.1.5 on 2025-02-15 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_alter_customusermodel_blood_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='blood_group',
            field=models.CharField(choices=[('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('A-', 'A-'), ('O-', 'O-'), ('O+', 'O+'), ('B-', 'B-')], max_length=3),
        ),
    ]
