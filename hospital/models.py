from django.db import models
from django.utils import timezone

# Create your models here.


class Patient(models.Model):
    hospital_no = models.CharField(max_length=10)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    date_of_birth = models.DateField(default=timezone.now)
    age = models.CharField(max_length=10)
    address = models.CharField(max_length=100, null=True, blank=True)
    mobile_number = models.CharField(max_length=15)
    ailment = models.CharField(max_length=100)

