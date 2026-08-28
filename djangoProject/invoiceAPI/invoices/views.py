from importlib.metadata import Lookup

from django.shortcuts import render
from rest_framework import viewsets
from .models import Customer, Invoice, InvoiceItem, Payment
from .serializers import (CustomerSerializer, InvoiceSerializer, InvoiceItemSerializer, PaymentSerializer,
InvoiceSerializer, InvoiceItemSerializer, PaymentSerializer)
from django.http import HttpResponse
from django.shortcuts import render

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

#Define home page:
def home(request):
    return render(request, "home.html")
    return HttpResponse("""
        <h1>Invoice & Payment Management API</h1>
        
        <p>
            A Django REST API for managing customers, invoices, invoice items, and payments.<br>
            This project provides CRUD functionality for creating, viewing, updating, and deleting customer invoice and payment data.
        </p>
        
        <h2>API Endpoints</h2>
        <ul>
            <li><a href = "/api/customers/">Customers</a></li>
            <li><a href = "/api/invoices/">Invoices</a></li>
            <li><a href = "/api/invoice-items/">Invoice Items</a></li>
            <li><a href = "/api/payments/">Payments</a></li>
            
        </ul>
        
        <footer>
        This Django site was developed by Andrew Koch.<br>
        All code along with a Docker containerization can be found at <a href="https://github.com/Andrew-Koch/Django-Docker">my github</a>        
        </footer>
    """)