from django.contrib import admin
from django.urls import path

from rest_framework.routers import DefaultRouter

from invoiceAPI.invoices.models import InvoiceItem
from views import (CustomerViewSet, InvoiceViewSet, InvoiceItemViewSet, PaymentViewSet)

#Create and configure URL patterns:
router = DefaultRouter
router.register("customers", CustomerViewSet)
router.register("invoices", InvoiceViewSet)
router.register("invoice-items", InvoiceItemViewSet)
router.register("payments", PaymentViewSet)

urlpatterns = router.urls

