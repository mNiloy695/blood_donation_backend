from . import models
from rest_framework import serializers
class RequestForBloodModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.RequestForBloodModel
        fields="__all__"

