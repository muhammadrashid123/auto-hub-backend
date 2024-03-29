from django.contrib.auth.models import User
from .models import *
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['username', ]



class certificationFilter(django_filters.FilterSet):

    are_expired = django_filters.DateFilter(field_name='expiry_date', lookup_expr='lte')
    class Meta:
        model = Certification
        
        fields = ['are_expired','certification_type', ]
