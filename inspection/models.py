
from django.db import models
from django.db.models.fields import EmailField, NullBooleanField
from django.contrib.auth.models import User
# Create your models here.

class Vehicle(models.Model):

    CATEGORY = (
        ("car", "car"),
        ("truck", "truck"),
        ("bus", "bus"),
    )

    reg_number = models.SlugField(max_length=8, null=True)
    vehicle_category = models.CharField(max_length=100, null=True, choices=CATEGORY)
    start_expl = models.DateField(null=True)

    def __str__(self):
        return self.reg_number

class Inspection(models.Model):

    CATEGORY = (
        ("Inspection Period Not Over", "Inspection Period Not Over"),
        ("Customer Notified Successfully", "Customer Notified Successfully"),
        ("Error Occurred Trying To Notify Customer", "Error Occurred Trying To Notify Customer"),
    )

    user= models.ForeignKey(User, null=True, blank = True, on_delete= models.CASCADE, related_name="inspections")
    vehicle = models.ForeignKey(Vehicle, null=True, blank=True, on_delete = models.SET_NULL, related_name="inspections")
    client_telnumber = models.CharField(max_length=10, null=True) 
    last_check = models.DateField(null=True)
    next_check = models.DateField(null=True)
    status = models.CharField(max_length=100, null=True, choices=CATEGORY)
    email  = models.EmailField(blank=True, null=True)
