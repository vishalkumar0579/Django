from django.db import models

# Create your models here.
class Courses(models.Model):
    Name = models.CharField(max_length=100,null=True)
    Trainer = models.CharField(max_length=100,null=True)
    Location = models.CharField(max_length=100,null=True)
    DAys = models.IntegerField(null=True)