from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator
from datetime import datetime


class Vehicle(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    service_interval = models.CharField(max_length=50)
    next_service = models.CharField(max_length=50)
    class Meta:
        abstract = True

class WheeledVehicle(Vehicle):
    seats = models.PositiveSmallIntegerField()
    color = models.CharField(max_length=100)
    VIN = models.CharField(max_length=17, validators=[MinLengthValidator(11)])
    current_mileage = models.PositiveSmallIntegerField()
    class Meta:
        abstract = True

class Car(WheeledVehicle):
    year = models.IntegerField(default=datetime.now().year, validators=[MinValueValidator(1886), MaxValueValidator(datetime.now().year)])


class Truck(WheeledVehicle):
    year = models.IntegerField(default=datetime.now().year, validators=[MinValueValidator(1896), MaxValueValidator(datetime.now().year)])
    bed_length = models.CharField(max_length=100)


class Boat(Vehicle):
    year = models.PositiveSmallIntegerField(default=datetime.now().year, validators=[MaxValueValidator(datetime.now().year)])
    length = models.CharField(max_length=100)
    width = models.CharField(max_length=100)
    HIN = models.CharField(max_length=14, validators=[MinLengthValidator(12)], blank=True)
    current_hours = models.PositiveSmallIntegerField()