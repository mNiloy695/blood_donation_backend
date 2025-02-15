from django.shortcuts import render

# Create your views here.
from .serializers  import DonateModelSerializer
from rest_framework.viewsets import ModelViewSet
from . import models
from rest_framework import  permissions
from urllib.parse import unquote

"""
 Set custom permission class for give permission more
 customizely the owner user 
"""
class IsOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print("Hello")
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            print(obj.user)
            print(f"Object owner: {obj.user.id}, Request user: {request.user.id}")
            return obj.user==request.user
        

class DonateModelView(ModelViewSet):
    
    serializer_class=DonateModelSerializer
    def get_permissions(self):
        # print(self.request.user.id)
        # permission handle for non user
        
        if not self.request.user.is_authenticated:
            
            if self.request.method in  ['GET']:
                
                return [permissions.AllowAny()]
            else:
                
                return [permissions.IsAuthenticated()]
                # return [permissions.AllowAny()]
            
        # permission handle for  user  but non admin
        # print(self.request.method)
        if self.request.user.is_authenticated  and not self.request.user.is_staff:
            # print(self.request.method)
            if self.request.method in ['GET','POST']:
                print(self.request.method)
                return [permissions.IsAuthenticated()]
            else:

                # if he is the Owner of the object then he can change
                print('yesss')
           
                
                return [IsOwnerPermission()]
                # return [permissions.AllowAny()]
            
        #admin will have all access

        return [permissions.IsAdminUser()]
    def get_queryset(self):
       
        request_id = self.kwargs.get('pk')
        print(request_id)
        queryset=models.DonationRequestModel.objects.all()
        user_id=self.request.query_params.get('user_id')
        blood_group=self.request.query_params.get('blood')

        """
        Return the queryset for DonateModelSerializer.
        Optionally filter by user_id if provided in the query params.
        """
        if  user_id:
            queryset=queryset.filter(user=user_id,status="Pending")
            return queryset
        if blood_group:
            blood_group=blood_group.replace(' ','+')
            print(blood_group)
            queryset=queryset.filter(blood=blood_group,status="Pending")
            print(queryset)
            return queryset
        else:
            # print(not self.request.user)
            if self.request.user.is_authenticated:
               if request_id:
                 queryset=queryset.filter(user=self.request.user)
               else:
                 if self.request.user.is_staff==True:
                     return queryset.filter()
                 else:
                    queryset=queryset.exclude(user=self.request.user)
               return queryset.filter(status="Pending")
            else:
                return queryset.filter(status="Pending")

