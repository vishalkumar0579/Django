from django.db import models
from django import forms

# Create your models here.
class FormValidations(models.Model):
    name_id      = models.IntegerField()
    name         = models.CharField(max_length=255)
    Phn_no       = models.IntegerField()
    feedback     = models.TextField(max_length=255)