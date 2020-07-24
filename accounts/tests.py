from django.test import TestCase
from rest_framework.test import APIClient
from django.test import Client

# Create your tests here.

class TestApi(TestCase):
    def testToken(self):
        c = Client()
        res = c.post('/api/token/', )
        print(res.data)

