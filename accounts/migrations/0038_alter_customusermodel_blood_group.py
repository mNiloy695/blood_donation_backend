# Generated by Django 5.1.5 on 2025-02-16 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0037_alter_customusermodel_blood_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='blood_group',
            field=models.CharField(choices=[('A-', 'A-'), ('AB+', 'AB+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('AB-', 'AB-'), ('B+', 'B+')], max_length=3),
        ),
    ]
