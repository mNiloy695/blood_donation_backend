# Generated by Django 5.1.5 on 2025-02-15 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestSpecific', '0028_alter_applybloodmodelforspecificuser_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applybloodmodelforspecificuser',
            name='status',
            field=models.CharField(choices=[('Cancelled', 'Cancelled'), ('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending', max_length=10),
        ),
    ]
