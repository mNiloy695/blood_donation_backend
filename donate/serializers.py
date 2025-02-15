from . import models
from rest_framework import serializers
from datetime import  date,timedelta
from rest_framework.response import Response
from django.utils import timezone

class DonateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.DonationRequestModel
        fields="__all__"
    
    def save(self):
        user=self.validated_data.get('user')
        status=self.validated_data.get('status')
        donateModel=self.instance
        donation=models.DonationRequestModel.objects.filter(user=user, status="Accepted")
        if(donateModel):
            if status:
                donateModel.status=status
                donateModel.save()
            return donateModel
        else:
            if(donation.exists() and not user.is_staff):
                if (date.today()-donation[0].last_donate)<timedelta(days=3*30):
                    raise serializers.ValidationError({"error":"You don't ready for donate,Please wait"})
                  
            elif( (date.today()-user.last_donation_date)<timedelta(days=3*30)):
                raise serializers.ValidationError({"error":"You don't ready for donate,Please wait"})
        # donation_request = models.DonationRequestModel.objects.create(**self.validated_data)
        # return donation_request
        donation_request = models.DonationRequestModel.objects.create(**self.validated_data)
        donation_request.last_donation=date.today()
        donation_request.save()
        if(donation_request.status=='Accepted'):
             user.last_donation=donation_request.last_donation
             user.save()

       
        print(donation_request)
        return donation_request
