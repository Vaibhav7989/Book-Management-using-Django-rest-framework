from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book
from django.urls import reverse
from .serializers import BookSerializer
# Create your tests here.

class Test_view(APITestCase):
    def test_list_view(self):
        response = self.client.get(reverse("Retrieving all the books"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_serializer_valid(self):
        data = {
        "id": 1,
        "title": "The woman in the window",
        "author": "A.J Finn",
        "price": "89.50",
        "quantity": 20}
        serializer = BookSerializer(data=data)
        self.assertTrue(serializer.is_valid())

