from django.db import models

# Create your models 

class Employee(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    salary = models.FloatField()
    city = models.CharField(max_length=50)