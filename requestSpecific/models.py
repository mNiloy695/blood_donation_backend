from django.db import models
from django.contrib.auth.models import User
from donate.models import DonationRequestModel
from requestForBlood.models import RequestForBloodModel
# Create your models here.
from django.contrib.auth  import get_user_model
User=get_user_model()
STATUS_TYPE={
    ('Pending','Pending'),
    ('Rejected','Rejected'),
    ('Accepted','Accepted'),
    ('Cancelled','Cancelled'),
}
class ApplyBloodModelForSpecificUser(models.Model):
    requester=models.ForeignKey(User,on_delete=models.CASCADE)
    blood_request=models.ForeignKey(DonationRequestModel,on_delete=models.CASCADE)
    created=models.DateField(auto_now_add=True)
    status=models.CharField(choices=STATUS_TYPE,default='Pending',max_length=10)
    blood_group=models.CharField(null=True,blank=True,max_length=5)
    phone=models.CharField(null=True,blank=True,max_length=12)

    """
    first i need to create a  request object then i pass it apply model from frontend
    """
    def __str__(self):
        return self.status
    def save(self,*args, **kwargs):
        self.blood_group=self.blood_request.blood
        self.phone=self.requester.phone
        if self.status=='Accepted':
            print("Yesss")
            
            self.blood_request.status='Accepted'
            self.blood_request.save()
            
            print("Yess 2")

        super().save(*args, **kwargs)
       