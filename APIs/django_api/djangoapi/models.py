from django.db import models
from django.db.models.fields import EmailField
from django.core.exceptions import ValidationError

#________ Validator ________#

def validateLength(value):
    if len(value) < 2:
        raise ValidationError(
            '{} must be longer than: 2'.format(value)
        )

#________ Classes ________#
class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Person(models.Model):
    first_name= models.CharField(max_length=45, validators=[validateLength])
    last_name= models.CharField(max_length=45, validators=[validateLength])
    age = models.IntegerField(null=True, blank=True)
    email = EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
