from rest_framework.test import APITestCase
from rest_framework import status
from .models import Customer
from django.test import TestCase

# Create your tests here.

#Test case for Customer:
class CustomerAPITest(APITestCase):

    #Test create customer:
    def test_create_customer(self):
        data = {
            "name": "Test Customer",
            "email": "Testcustomer@test.com"
        }
        response = self.client.post("/api/customers/", data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)

    #Test get customer:
    def test_get_customer(self):
        customer = Customer.objects.create(
            name = "Test Customer",
            email = "Testcustomer@test.com"
        )
        response = self.client.get(f"/api/customers/{customer.id}/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Test Customer")

    #Test update customer:
    def test_update_customer(self):
        customer = Customer.objects.create(
            name="Test Customer",
            email="Testcustomer@test.com"
        )

        data = {
            "name": "Updated Customer",
            "email": "updatedcustomer@test.com"
        }
        response = self.client.put(f"/api/customers/{customer.id}/", data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Updated Customer")

    #Test delete customer:
    def test_delete_customer(self):
        customer = Customer.objects.create(
            name="Test Customer",
            email="Testcustomer@test.com"
        )

        response = self.client.delete(f"/api/customers/{customer.id}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Customer.objects.count(), 0)


