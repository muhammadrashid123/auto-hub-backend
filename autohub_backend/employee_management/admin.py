from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(DriverProfile)
admin.site.register(CertificationProvider)
admin.site.register(CertificationType)
admin.site.register(Certification)
admin.site.register(VehicleType)
admin.site.register(JobType)
admin.site.register(Job)
admin.site.register(DriverHistory)