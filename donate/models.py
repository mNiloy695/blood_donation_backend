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
class DonationRequestModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=10,choices=STATUS_TYPE,default='Pending')
    blood=models.CharField(choices=BLOOD_GROUP,max_length=3)
    address=models.CharField(max_length=200,blank=True,null=True)
    phone=models.CharField(max_length=100,blank=True,null=True)
    unit=models.IntegerField(default=1,blank=True,null=True)
    last_donate=models.DateField(blank=True,null=True)
    email=models.EmailField(blank=True,null=True)
    def __str__(self):
       return f"{self.status} {self.blood}"
    class Meta:
        ordering=['last_donate']
    
    def save(self, *args, **kwargs):
      if not self.email:
        self.email = self.user.email
      super().save(*args, **kwargs)

