from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
import rest_framework
from rest_framework.parsers import JSONParser 
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from django.contrib.auth.models import User
from django_filters import rest_framework as filters
from .filter import *


# Create your views here.

class UserViewSet(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

    serializer_class = UserSerializer
    queryset = User.objects.all()

    lookup_field = 'id'

    def get(self, request, id = None):
        if id:
            return self.retrieve(request)
        else:  
            return self.list(request)

    def post(self, request):

        return self.create(request)

    def put(self, request, id = None):
        return self.update(request, id)

    def delete(self,request, id):
        return self.destroy(request, id)


class ProfileViewSet(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

    serializer_class = ProfileSerializer
    queryset = DriverProfile.objects.all()

    lookup_field = 'id'

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('user',)

    def get(self, request, id = None):
        if id:
            return self.retrieve(request)
        else:    
            return self.list(request)

    def post(self, request):

        return self.create(request)

    def put(self, request, id = None):
        return self.update(request, id)

    def delete(self,request, id):
        return self.destroy(request, id)

class CertificationProviderViewSet(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

    serializer_class = CertificationProviderSerializer
    queryset = CertificationProvider.objects.all()

    lookup_field = 'id'

    def get(self, request, id = None):
        if id:
            return self.retrieve(request)
        else:    
            return self.list(request)

    def post(self, request):

        return self.create(request)

    def put(self, request, id = None):
        return self.update(request, id)

    def delete(self,request, id):
        return self.destroy(request, id)


class CertificationTypeViewSet(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
 
    serializer_class = CertificationTypeSerializer
    queryset = CertificationType.objects.all()

    lookup_field = 'id'
    

    def get(self, request, id = None):
        if id:
            return self.retrieve(request)
        else:    
            return self.list(request)

    def post(self, request):

        return self.create(request)

    def put(self, request, id = None):
        return self.update(request, id)

    def delete(self,request, id):
        return self.destroy(request, id)


class CertificationViewSet(generics.ListAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

    serializer_class = CertificationSerializer
    queryset = Certification.objects.all()

    lookup_field = 'id'
    
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = (certificationFilter)
    
    # filterset_fields = ('expiry_date','issue_date','certification_type', 'user',)

    def get(self, request, id = None):
        
        if id:
            return self.retrieve(request)
        else:    
            return self.list(request)

    def post(self, request):

        return self.create(request)

    def put(self, request, id = None):
        return self.update(request, id)

    def delete(self,request, id):
        return self.destroy(request, id)


class VehicleTypeViewSet(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

    serializer_class = VehicleTypeSerializer
    queryset = VehicleType.objects.all()

    lookup_field = 'id'

    def get(self, request, id = None):
        if id:
            return self.retrieve(request)
        else:    
            return self.list(request)

    def post(self, request):

        return self.create(request)

    def put(self, request, id = None):
        return self.update(request, id)

    def delete(self,request, id):
        return self.destroy(request, id)


class JobTypeViewSet(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

    serializer_class = JobTypeSerializer
    queryset = JobType.objects.all()

    lookup_field = 'id'
    

    def get(self, request, id = None):
        if id:
            return self.retrieve(request)
        else:    
            return self.list(request)

    def post(self, request):

        return self.create(request)

    def put(self, request, id = None):
        return self.update(request, id)

    def delete(self,request, id):
        return self.destroy(request, id)

class JobViewSet(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

    serializer_class = JobSerializer
    queryset = Job.objects.all()

    lookup_field = 'id'

    def get(self, request, id = None):
        if id:
            return self.retrieve(request)
        else:    
            return self.list(request)

    def post(self, request):

        return self.create(request)

    def put(self, request, id = None):
        return self.update(request, id)

    def delete(self,request, id):
        return self.destroy(request, id)

class DriverHistoryViewSet(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

    serializer_class = DriverHistorySerializer
    queryset = DriverHistory.objects.all()

    lookup_field = 'id'
    filter_backends = (filters.DjangoFilterBackend,)
    
    filterset_fields = ('driver',)

    def get(self, request, id = None):
        if id:
            return self.retrieve(request)
        else:    
            return self.list(request)

    def post(self, request):

        return self.create(request)

    def put(self, request, id = None):
        return self.update(request, id)

    def delete(self,request, id):
        return self.destroy(request, id)