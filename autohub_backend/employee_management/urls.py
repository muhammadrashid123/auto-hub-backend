from django.urls import path
from .views import *

urlpatterns = [
     path ('user/', UserViewSet.as_view()),
     path('profile/', ProfileViewSet.as_view()),
     path('profile/<int:id>/', ProfileViewSet.as_view()),
     path('certification/', CertificationViewSet.as_view()),
     path('certification/<int:id>/', CertificationViewSet.as_view()),
     path('certificationtype/', CertificationTypeViewSet.as_view()),
     path('certificationtype/<int:id>/', CertificationTypeViewSet.as_view()),
     path('certificationprovider/', CertificationProviderViewSet.as_view()),
     path('certificationprovider/<int:id>/', CertificationProviderViewSet.as_view()),
     path('vehicletype/', VehicleTypeViewSet.as_view()),
     path('vehicletype/<int:id>/', VehicleTypeViewSet.as_view()),
     path('jobtype/', JobTypeViewSet.as_view()),
     path('jobtype/<int:id>/', JobTypeViewSet.as_view()),
     path('job/', JobViewSet.as_view()),
     path('job/<int:id>/', JobViewSet.as_view()),
     path('driverhistory/', DriverHistoryViewSet.as_view()),
     path('driverhistory/<int:id>/', DriverHistoryViewSet.as_view()),

]