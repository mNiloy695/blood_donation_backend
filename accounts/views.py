from django.shortcuts import render,redirect

# Create your views here.
from . import serializers
from rest_framework import viewsets
from  .models import CustomUserModel
from rest_framework import permissions
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token


class IsOwnerObjectAllowAll(permissions.BasePermission):
     def has_object_permission(self, request, view, obj):
          if request.method in permissions.SAFE_METHODS:
               return True
          return obj.id==request.user.id
class RegistrationView(viewsets.ModelViewSet):
    queryset=CustomUserModel.objects.all()
    serializer_class=serializers.CustomUserRegistrationSerializer

    def get_permissions(self):
         user=self.request.user 
         if not user.is_authenticated:
              if self.request.method in ['GET','POST']:
                   return [permissions.AllowAny()]
              else:
                   return [permissions.IsAuthenticated()]
         if not  user.is_staff:
              if self.request.method in ['GET','PUT','PATCH','DELETE']:
                   return [IsOwnerObjectAllowAll()]
              else:
                   return [permissions.IsAdminUser()]
         else:
              return [permissions.IsAdminUser()]
         
        
         return super().get_permissions()
    def perform_create(self, serializer):
        user = serializer.save() # Save the user first # Generate token and send confirmation email 
        token = default_token_generator.make_token(user) 
        uid = urlsafe_base64_encode(force_bytes(user.pk)) 
        confirmation_link = f'http://127.0.0.1:8000/account/activate/{uid}/{token}/' 
        subject = "Confirmation Mail" 
        body = render_to_string('confirmation_mail.html', {'confirmation_link': confirmation_link})
        email = EmailMultiAlternatives(subject, '', to=[user.email])
        email.attach_alternative(body, 'text/html') 
        print("yeeeeessssssss !!!!!")
        email.send() 
        return Response(serializer.data, status=201)    
    
  
            
def activate(request,uid64,token):
    try:
        uid=urlsafe_base64_decode(uid64).decode()
        user=CustomUserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError,CustomUserModel.DoesNotExist):
        user=None
    if user is not None and default_token_generator.check_token(user,token):
            user.is_active=True
            user.save()
            return redirect('https://blood-donation-frontend-chi.vercel.app/login')
        
    return redirect('https://blood-donation-frontend-chi.vercel.app/register')


# login serializer 


class UserLoginViewSet(APIView):
    serializer_class=serializers.UserLoginSerializer
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            username=serializer.validated_data['username']
            password=serializer.validated_data['password']
            user=authenticate(username=username,password=password)
            if user:
                token,_=Token.objects.get_or_create(user=user)
                login(request,user)
                if user.is_staff:
                     redirect('https://blood-donation-frontend-chi.vercel.app/dashboard')
                redirect('https://blood-donation-frontend-chi.vercel.app/')
                
                return Response({'token':token.key,'user_id':user.id,"is_staff":user.is_staff,"blood_group":user.blood_group})
            else:
                return Response({'error':'invalid user'})
        else:
            return Response(serializer.errors)
class UserLogoutViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request):
        logout(request)
        redirect('https://blood-donation-frontend-chi.vercel.app/login')
        return Response({'detail':"Successfully logout"})
