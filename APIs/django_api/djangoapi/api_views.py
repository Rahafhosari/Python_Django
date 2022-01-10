from django.db.models import query
from rest_framework import response
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, UpdateAPIView, \
    RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.exceptions import ValidationError
from djangoapi.serializers import PersonSerializer
from djangoapi.models import *

class PersonPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 20

class PersonList(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id',)
    search_fields = ('id','first_name','age')
    pagination_class = PersonPagination


class PersonCreate(CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

'''The Retrieve Update Destroy is used instead'''
# class PersonDestroy(DestroyAPIView):
#     queryset = Person.objects.all()
#     lookup_field = 'id'
#     def delete(self, request, *args, **kwargs):
#         person_id = request.data.get('id')
#         response = super().delete(request,*args,**kwargs)
#         if response.status_code == 204:
#             from django.core.cache import cache
#             cache.delete('person_data_{}'.format(person_id))
#         return response


#_____ Retireive Update API View _____#
class PersonRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    lookup_field = 'id'
    serializer_class = PersonSerializer

    def delete(self, request, *args, **kwargs):
        person_id = request.data.get('id')
        response = super().delete(request,*args,**kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('person_data_{}'.format(person_id))
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            person = response.data
            cache.set('person_data_{}'.format(person['id']), {
                'first_name':person['first_name'],
                'last_name':person['last_name'],
                'age':person['age'],
                'email':person['email'],
            })
        return response