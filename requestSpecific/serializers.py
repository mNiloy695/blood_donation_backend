from .models import ApplyBloodModelForSpecificUser
from  rest_framework import serializers


class ApplyBloodSerializerForSpecificUser(serializers.ModelSerializer):
    class Meta:
        model=ApplyBloodModelForSpecificUser
        fields="__all__"
        