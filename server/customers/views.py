

from customers.models import Customer
from customers.serializers import CustomerSerializer
from rest_framework import viewsets
from rest_framework.response import Response
import django_filters.rest_framework
from rest_framework import filters


class CustomerViewSet(viewsets.ModelViewSet):
    
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'age')
