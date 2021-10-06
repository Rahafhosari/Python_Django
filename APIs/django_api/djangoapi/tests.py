# from django.test import TestCase

from re import A
from rest_framework import response
from rest_framework.test import APITestCase
from djangoapi.models import *

# Create your tests here.
class PersonCreateTestCase(APITestCase):
    def test_create_person(self):
        initial_person_count = Person.objects.count()
        person_attrs = {
            'first_name':'Axsosian',
            'last_name':'Axsos_Academy',
            'age': 1,
            'email':'axsos@gmail.com',
        }
        response = self.client.post('api/v1/people/new',person_attrs)
        # if response.status_code != 201:
            # print(response.data)
        # self.assertEqual(
        #     Person.objects.count(),
        #     initial_person_count + 1,
        # )
