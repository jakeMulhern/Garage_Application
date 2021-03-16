from rest_framework import serializers
from garage_inventory.models import Car, Truck, Boat
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator
from django.contrib.auth.models import User


class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
      model = Car
      fields = ['url', 'id', 'make', 'model', 'year', 'seats', 'color', 'VIN', 'current_mileage', 'service_interval', 'next_service']


class TruckSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Truck
        fields = ['url', 'id', 'make', 'model', 'year', 'seats', 'bed_length', 'color', 'VIN', 'current_mileage', 'service_interval', 'next_service']


class BoatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Boat
        fields = ['url', 'id', 'make', 'model', 'year', 'length', 'width', 'HIN', 'current_hours', 'service_interval', 'next_service']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username']