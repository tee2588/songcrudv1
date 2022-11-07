from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Artiste
from .serializers import ArtisteSerializer

# Create your tests here.

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_artiste(first_name="", last_name="", age=""):
        if first_name != "" and last_name != "" and age != "":
            Artiste.objects.create(first_name=first_name, last_name=last_name, age=age)

    def setUp(self):
        # add test data
        self.create_artiste("David Davido", "Adeleke", 30)
        self.create_artiste("Ayo Wizkid", "Balogun", 34)
        self.create_artiste("Ahmed Asake", "Ololade", 27)
        self.create_artiste("Bukola Asa", "Elemide", 40)
        self.create_artiste("Jude MI", "Abaga", 41)

class GetAllArtisteTest(BaseViewTest):

    def test_get_all_artiste(self):
        """
        This test ensures that all artistes added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("artiste-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Artiste.objects.all()
        serialized = ArtisteSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)