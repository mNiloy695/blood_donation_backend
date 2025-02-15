from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import RequestForBloodModelView

router=DefaultRouter()
router.register('request',RequestForBloodModelView,basename='recive')

urlpatterns = [
    
    path('',include(router.urls)),
]
