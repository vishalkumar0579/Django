from django.db import models
from Webapp.models import FormValidations
from django import forms

class validation(forms.ModelForm):
    class Meta:
        model=FormValidations
        fields='__all__'

class validationLimit(forms.ModelForm):
    class Meta:
        model=FormValidations
        fields=['name','Phn_no','feedback']