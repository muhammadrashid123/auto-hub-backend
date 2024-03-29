
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Employee management app urls
    #path('employee-management/', include('employee_management.urls')),

]

