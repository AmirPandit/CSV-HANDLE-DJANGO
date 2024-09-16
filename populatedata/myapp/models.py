from django.db import models
from rest_framework.response import Response
    
class Book(models.Model):
    title = models.CharField(max_length=125)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=250)
    description = models.TextField(help_text="Description of the book here.")
    publish_date = models.CharField(max_length=125, null=True)
    category = models.CharField(max_length=125)
    
    def __str__(self):
        return self.title