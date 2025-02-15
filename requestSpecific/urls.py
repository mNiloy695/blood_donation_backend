from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import  ApplySerializerForSpecificUserView

router=DefaultRouter()
router.register('specificRequest', ApplySerializerForSpecificUserView,basename='apply')

urlpatterns = [
    path('',include(router.urls)),
]
