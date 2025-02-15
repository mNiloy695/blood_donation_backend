from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

BLOOD_GROUP={
    ('A+','A+'),
    ('A-','A-'),
    ('AB+','AB+'),
    ('AB-','AB-'),
    ('B+','B+'),
    ('B-','B-'),
    ('O+','O+'),
    ('O-','O-'),
}
class CustomUserModel(AbstractUser):
    blood_group=models.CharField(max_length=3,choices=BLOOD_GROUP)
    last_donation_date=models.DateField(default='2024-01-01')
    phone=models.CharField(max_length=14)
  