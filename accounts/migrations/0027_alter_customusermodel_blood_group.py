# Generated by Django 5.1.5 on 2025-02-15 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0026_alter_customusermodel_blood_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='blood_group',
            field=models.CharField(choices=[('AB+', 'AB+'), ('B-', 'B-'), ('A+', 'A+'), ('AB-', 'AB-'), ('B+', 'B+'), ('A-', 'A-'), ('O+', 'O+'), ('O-', 'O-')], max_length=3),
        ),
    ]
