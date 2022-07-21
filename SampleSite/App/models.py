# import the standard Django Model
# from built-in library
from django.db import models

# Create your models here.
class LokeshModel(models.Model):
    #Feilds of Models:
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
