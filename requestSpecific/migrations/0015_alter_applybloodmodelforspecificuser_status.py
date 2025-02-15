# Generated by Django 5.1.5 on 2025-02-11 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestSpecific', '0014_alter_applybloodmodelforspecificuser_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applybloodmodelforspecificuser',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Rejected', 'Rejected'), ('Pending', 'Pending'), ('Cancelled', 'Cancelled')], default='Pending', max_length=10),
        ),
    ]
