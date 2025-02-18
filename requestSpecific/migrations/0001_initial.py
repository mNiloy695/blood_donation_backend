# Generated by Django 5.1.5 on 2025-01-18 15:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('donate', '0006_alter_donationrequestmodel_blood_and_more'),
        ('requestForBlood', '0002_alter_requestforbloodmodel_blood_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyBloodModelForSpecificUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Cancelled', 'Cancelled'), ('Rejected', 'Rejected'), ('Pending', 'Pending'), ('Accepted', 'Accepted')], default='Pending', max_length=10)),
                ('blood_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requestForBlood.requestforbloodmodel')),
                ('donate_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donate.donationrequestmodel')),
            ],
        ),
    ]
