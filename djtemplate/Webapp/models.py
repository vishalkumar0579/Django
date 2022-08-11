from django.db import models

# Create your models here.

class FilterModel(models.Model):
    name=models.CharField(max_length=200)
    Subject=models.CharField(max_length=200)
    dept=models.CharField(max_length=200)
    date = models.DateField()
