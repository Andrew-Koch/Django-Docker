from symtable import Class

from django.db import models

# Create your models here.

#Define customers:
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Invoice(models.Model):
    issue_date = models.DateField()
    due_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    #When customer is deleted, delete all invoices for customer:
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"Invoice #{self.id}"

class InvoiceItem(models.Model):
    description = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    #When invoice is deleted, delete all invoice items:
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name="items")
    def __str__(self):
        return self.description

class Payment(models.Model):
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    #When invoice is deleted, delete all invoice payments:
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name="payments")

    def __str__(self):
        return f"Payment #{self.id}"