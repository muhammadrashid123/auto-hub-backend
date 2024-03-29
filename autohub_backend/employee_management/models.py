from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class DriverProfile(models.Model):
    CNIC = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=80)
    address = models.TextField(default='')
    experience = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class CertificationProvider(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(default='')
    rating = models.IntegerField()

    def __str__(self):
        return self.name

class CertificationType(models.Model):
    type_name = models.CharField(max_length=100)

    def __str__(self):
        return self.type_name

class Certification(models.Model):

    certification_type = models.ForeignKey(CertificationType,   on_delete=models.CASCADE , default='')
    certification_provider = models.ForeignKey(CertificationProvider,  on_delete=models.CASCADE)
    issue_date =  models.DateField()
    expiry_date = models.DateField()
    certification_number = models.CharField(max_length=100)
    user = models.ForeignKey(User,  on_delete=models.CASCADE)

    def __str__(self):
        return self.user

class VehicleType(models.Model):
    type_name = models.CharField(max_length=100)

    def __str__(self):
        return self.type_name

class JobType(models.Model):
    vehicle_type = models.ForeignKey(VehicleType,  on_delete=models.CASCADE)
    certification_type = models.ManyToManyField(CertificationType)

    def __str__(self):
        return self.certification_type

class Job(models.Model):
    start_date =  models.DateTimeField(auto_now=False, auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    vehicle_type = models.ForeignKey(VehicleType,  on_delete=models.CASCADE)
    job = models.TextField(default='')

    def __str__(self):
        return self.job

class DriverHistory(models.Model):
    driver = models.ForeignKey(DriverProfile,  on_delete=models.CASCADE)
    vehicle = models.ForeignKey(VehicleType,  on_delete=models.CASCADE)
    start_date =  models.DateTimeField(auto_now=False, auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.driver