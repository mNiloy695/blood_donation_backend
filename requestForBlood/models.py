from django.shortcuts import render

# Create your views here.
from django.db import models
from  django.contrib.auth.models import User
from django.contrib.auth  import get_user_model
User=get_user_model()
# Create your models here.

STATUS_TYPE={
    ('Pending','Pending'),
    ('Rejected','Rejected'),
    ('Accepted','Accepted'),
    ('Cancelled','Cancelled'),
}
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
class RequestForBloodModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=10,choices=STATUS_TYPE,default='Pending')
    blood=models.CharField(choices=BLOOD_GROUP,max_length=3)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=100)
    unit=models.IntegerField(default=1)
    def __str__(self):
        return f"user {self.user.username} {self.blood}"
    