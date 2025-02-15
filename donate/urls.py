from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import DonateModelView
router=DefaultRouter()
router.register('request',DonateModelView,basename='donate')

urlpatterns = [
    path('',include(router.urls)),
]
