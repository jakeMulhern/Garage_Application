from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator
from datetime import datetime


class Car(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(default=2021, validators=[MinValueValidator(1886), MaxValueValidator(datetime.now().year)])
    seats = models.PositiveSmallIntegerField()
    color = models.CharField(max_length=100)
    VIN = models.CharField(max_length=17, validators=[MinLengthValidator(11)])
    current_mileage = models.PositiveSmallIntegerField()
    service_interval = models.CharField(max_length=50)
    next_service = models.CharField(max_length=50)


class Truck(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(default=datetime.now().year, validators=[MinValueValidator(1886), MaxValueValidator(datetime.now().year)])
    seats = models.PositiveSmallIntegerField()
    bed_length = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    VIN = models.CharField(max_length=17, validators=[MinLengthValidator(11)])
    current_mileage = models.PositiveSmallIntegerField()
    service_interval = models.CharField(max_length=50)
    next_service = models.CharField(max_length=50)


class Boat(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField(default=datetime.now().year, validators=[MaxValueValidator(datetime.now().year)])
    length = models.CharField(max_length=100)
    width = models.CharField(max_length=100)
    HIN = models.CharField(max_length=14, validators=[MinLengthValidator(12)], blank=True)
    current_hours = models.PositiveSmallIntegerField()
    service_interval = models.CharField(max_length=50)
    next_service = models.CharField(max_length=50)