# Generated by Django 5.1.5 on 2025-02-16 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestSpecific', '0035_alter_applybloodmodelforspecificuser_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applybloodmodelforspecificuser',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Cancelled', 'Cancelled'), ('Rejected', 'Rejected'), ('Pending', 'Pending')], default='Pending', max_length=10),
        ),
    ]
