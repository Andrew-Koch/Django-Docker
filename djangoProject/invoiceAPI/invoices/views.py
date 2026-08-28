from django.shortcuts import render
from rest_framework import viewsets
from .models import Customer, Invoice, InvoiceItem, Payment
from .serializers import (CustomerSerializer, InvoiceSerializer, InvoiceItemSerializer, PaymentSerializer,
InvoiceSerializer, InvoiceItemSerializer, PaymentSerializer)

# Create your views here.

#Add CRUD functionality to Customer model class:
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

#Add CRUD functionality to Invoice model class:
class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

#Add CRUD functionality to InvoiceItem model class:
class InvoiceItemViewSet(viewsets.ModelViewSet):
    queryset = InvoiceItem.objects.all()
    serializer_class = InvoiceItemSerializer

#Add CRUD functionality to Payment model class:
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
