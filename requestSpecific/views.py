from django.shortcuts import render
from rest_framework import permissions
# Create your views here.
from .serializers import ApplyBloodSerializerForSpecificUser
from rest_framework  import viewsets
from .models import ApplyBloodModelForSpecificUser
class IsOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return  True
        return obj.donate_request.user==request.user
class ApplySerializerForSpecificUserView(viewsets.ModelViewSet):
    serializer_class=ApplyBloodSerializerForSpecificUser
 


    def get_permissions(self):
        user=self.request.user
        if not user.is_authenticated:
            return [permissions.IsAuthenticated()]
        if user.is_authenticated and not user.is_staff:
            if self.request.method in ['GET','POST']:
                return [permissions.AllowAny()]
            else:
                return [IsOwnerPermission()]
        if user.is_authenticated and user.is_staff:
            return [permissions.IsAdminUser()]
    
    def get_queryset(self):
        queryset=ApplyBloodModelForSpecificUser.objects.all()
        user_id=self.request.query_params.get('user_id')
        if user_id:
         
            return queryset.filter(blood_request__user=user_id)
        return queryset
            