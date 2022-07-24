# import the standard Django Model
# from built-in library
from django.db import models

# Create your models here.
class State_details(models.Model):
    #Feilds of Models:
    Name = models.CharField(max_length=30)
    Address = models.CharField(max_length=50)
    City = models.CharField(max_length=20)

    def __str__(self):
        return self.City
