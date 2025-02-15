from .models import CustomUserModel
from rest_framework import serializers
from .models import CustomUserModel
from rest_framework import serializers

class CustomUserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUserModel
        fields = ['id', 'username', 'email', 'last_donation_date', 'first_name', 'last_name', 'phone', 'blood_group', 'password', 'confirm_password']

    def save(self):
        # Get validated data
        username = self.validated_data.get('username', None)
        password = self.validated_data.get('password', None)
        first_name = self.validated_data.get('first_name', None)
        last_name = self.validated_data.get('last_name', None)
        email = self.validated_data.get('email', None)
        last_donation_date = self.validated_data.get('last_donation_date','2024-01-01')
        confirm_password = self.validated_data.get('confirm_password', None)
        phone = self.validated_data.get('phone', None)
        blood_group = self.validated_data.get('blood_group', None)
       

        # Validate password confirmation
        if password and confirm_password:
                if password != confirm_password:
                  raise serializers.ValidationError({'error': "Your confirm password doesn't match"})

        # Check if user exists or if it's a new one
        user = self.instance if self.instance else None
        if user:
            # Update the existing user
            print(user)
            if password:
                user.set_password(password)  # Update password if provided
            if username and user.username != username:
                if CustomUserModel.objects.filter(username=username).exists():
                    raise serializers.ValidationError({'error': "This username already exists"})
                user.username = username
            if email and user.email != email:
                if CustomUserModel.objects.filter(email=email).exists():
                    raise serializers.ValidationError({'error': "This email already exists"})
                user.email = email
            if phone:
                user.phone = phone
            if blood_group:
                user.blood_group = blood_group
            if first_name != user.first_name:
                user.first_name = first_name
            if last_name != user.last_name:
                user.last_name = last_name
            if last_donation_date != user.last_donation_date:
                user.last_donation_date = last_donation_date

            user.save()
        else:
            
            # Create a new user
            user = CustomUserModel(
                username=username,
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                blood_group=blood_group,
                email=email,
                last_donation_date=last_donation_date
            )
            user.set_password(password)
            user.is_active = False  # Deactivate user initially
            user.save()

        return user


class UserLoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()
    