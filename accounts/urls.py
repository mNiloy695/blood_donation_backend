from django.urls import path,include

from rest_framework.routers import DefaultRouter
from .views import RegistrationView,activate,UserLoginViewSet,UserLogoutViewSet
router =DefaultRouter()

router.register('register',RegistrationView,basename='register')

urlpatterns = [
     path('',include(router.urls)),
     path('activate/<uid64>/<token>/',activate,name='activate'),
     path('login/',UserLoginViewSet.as_view(),name='login'),
     path('logout/',UserLogoutViewSet.as_view(),name='logout'),
]
