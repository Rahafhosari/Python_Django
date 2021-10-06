from django.db.models import fields
from rest_framework import serializers
from djangoapi.models import *

#________ Article Model ________#
# class ArticleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = ('id','title','text','image','created_at','updated_at')

#     def to_read(self,instance):
#         data = super().to_read(instance)
#         data['is_it_read'] = instance.is_it_read()
#         # data['current_state'] = instance.current_state()
#         return data

#________ Person Model ________#
class PersonSerializer(serializers.ModelSerializer):
    # is_registered = serializers.BooleanField(read_only=True)
    # description = serializers.CharField(min_length=2, max_length=200)
    
    class Meta:
        model = Person
        fields = ('id','first_name','last_name','age','email','created_at','updated_at')

    # def to_representation(self,instance):
    #     data = super().to_representation(instance)
    #     data['is_registered'] = instance.is_registered()
    #     return data

