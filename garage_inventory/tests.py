from .models import Car, Truck, Boat

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate, APIClient
from django.contrib.auth.models import User


class CarTests(APITestCase):
    def setUp(self):
        self.username = 'admin'
        self.password = 'password123'
        self.user = User.objects.create(username=self.username, password=self.password)
        self.client.force_authenticate(user=self.user)

    def test_get_car_list(self):
        """
        Ensure that we are able to get a readable list of all the car objects.
        """
        new_car = Car.objects.create(make='Chevy', model='Equinox', year=2012, seats=4, color='green', VIN='12345671234567abc', current_mileage=19000, service_interval=3, next_service='april')
        url = reverse('car-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_car_list_returns_401_status_code_without_authentication(self):
        """
        Ensure that we are not able to get a readable list of all the car objects without authorization.
        """
        self.client.force_authenticate(user=None)
        new_car = Car.objects.create(make='Chevy', model='Equinox', year=2012, seats=4, color='green', VIN='12345671234567abc', current_mileage=19000, service_interval=3, next_service='april')
        url = reverse('car-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_car_detail(self):
        """
        Ensure that we are able to get each car's details.
        """
        new_car = Car.objects.create(make='Chevy', model='Equinox', year=2012, seats=4, color='green', VIN='12345671234567abc', current_mileage=19000, service_interval=3, next_service='april')
        url = reverse('car-detail', kwargs={'pk': new_car.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_car_detail_returns_401_status_code_without_authentication(self):
        """
        Ensure that we are not able to get each car's details without authorization.
        """
        self.client.force_authenticate(user=None)
        new_car = Car.objects.create(make='Chevy', model='Equinox', year=2012, seats=4, color='green', VIN='12345671234567abc', current_mileage=19000, service_interval=3, next_service='april')
        url = reverse('car-detail', kwargs={'pk': new_car.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_car(self):
        """
        Ensure that we are able to create a new car object.
        """
        url = reverse('car-list')
        data = {
            'make': 'Chevy',
            'model': 'Equinox',
            'year': 2014,
            'seats': 5,
            'color': 'blue',
            'VIN': '12345671234567abc',
            'current_mileage': 20000,
            'service_interval': 3,
            'next_service': 'July',
        }
        initial_car_count = Car.objects.count()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Car.objects.count(), initial_car_count + 1)
        self.assertEqual(Car.objects.get().make, 'Chevy')
    
    def test_create_car_returns_401_status_code_without_authorization(self):
        """
        Ensure that we are not able to create a new car object without authorization.
        """
        self.client.force_authenticate(user=None)
        url = reverse('car-list')
        data = {
            'make': 'Chevy',
            'model': 'Equinox',
            'year': 2014,
            'seats': 5,
            'color': 'blue',
            'VIN': '12345671234567abc',
            'current_mileage': 20000,
            'service_interval': 3,
            'next_service': 'July',
        }
        initial_car_count = Car.objects.count()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Car.objects.count(), initial_car_count)
    
    def test_update_car(self):
        """
        Ensure that we are able to update car objects.
        """
        new_car = Car.objects.create(make='Chevy', model='Equinox', year=2012, seats=4, color='green', VIN='12345671234567abc', current_mileage=19000, service_interval=3, next_service='april')
        url = reverse('car-detail', kwargs={'pk': new_car.pk})
        data = {
            'make': 'test',
            'model': 'test',
            'year': 2014,
            'seats': 5,
            'color': 'blue',
            'VIN': '12345671234567abc',
            'current_mileage': 20000,
            'service_interval': 6,
            'next_service': 'July',
        }
        self.assertEqual(new_car.make, 'Chevy')
        response = self.client.put(url, data=data)
        new_car.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(new_car.make, 'test')
    
    def test_update_car_returns_401_status_code_without_authorization(self):
        """
        Ensure that we are able to update car objects.
        """
        new_car = Car.objects.create(make='Chevy', model='Equinox', year=2012, seats=4, color='green', VIN='12345671234567abc', current_mileage=19000, service_interval=3, next_service='april')
        url = reverse('car-detail', kwargs={'pk': new_car.pk})
        data = {
            'make': 'test',
            'model': 'test',
            'year': 2014,
            'seats': 5,
            'color': 'blue',
            'VIN': '12345671234567abc',
            'current_mileage': 20000,
            'service_interval': 6,
            'next_service': 'July',
        }
        self.client.force_authenticate(user=None)
        self.assertEqual(new_car.make, 'Chevy')
        response = self.client.put(url, data=data)
        new_car.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(new_car.make, 'Chevy')
    
    def test_delete_car(self):
        """
        Ensure that we are able to delete a car object.
        """
        new_car = Car.objects.create(make='Chevy', model='Equinox', year=2012, seats=4, color='green', VIN='12345671234567abc', current_mileage=19000, service_interval=3, next_service='april')
        initial_car_count = Car.objects.count()
        url = reverse('car-detail', kwargs={'pk': new_car.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Car.objects.count(), initial_car_count - 1)
    
    def test_delete_car_returns_401_status_code_without_authorization(self):
        """
        Ensure that we are able to delete a car object.
        """
        new_car = Car.objects.create(make='Chevy', model='Equinox', year=2012, seats=4, color='green', VIN='12345671234567abc', current_mileage=19000, service_interval=3, next_service='april')
        initial_car_count = Car.objects.count()
        self.client.force_authenticate(user=None)
        url = reverse('car-detail', kwargs={'pk': new_car.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Car.objects.count(), initial_car_count)


class TruckTests(APITestCase):
    def setUp(self):
        self.username = 'admin'
        self.password = 'password123'
        self.user = User.objects.create(username=self.username, password=self.password)
        self.client.force_authenticate(user=self.user)

    def test_get_truck_list(self):
        """
        Ensure that we are able to get a readable list of all the truck objects.
        """
        new_truck = Truck.objects.create(make='Ford', model='Bronco', year=1981, seats=4, bed_length="4 ft", color='orange', VIN='12345671234567abc', current_mileage=19000, service_interval=3, next_service='april')
        url = reverse('truck-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Truck.objects.count(), 1)
    
    def test_get_truck_list_returns_401_status_code_without_authentication(self):
        """
        Ensure that we are not able to get a readable list of all the truck objects without authentication.
        """
        new_truck = Truck.objects.create(make='Ford', model='Bronco', year=1981, seats=4, bed_length="4 ft", color='orange', VIN='12345671234567abc', current_mileage=19000, service_interval=3, next_service='april')
        self.client.force_authenticate(user=None)
        url = reverse('truck-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_get_truck_detail(self):
        """
        Ensure that we are able to get each trucks's details.
        """
        new_truck = Truck.objects.create(make='Ford', model='Bronco', year=1981, seats=4, bed_length="4 ft", color='orange', VIN='12345671234567abc', current_mileage=19000, service_interval=3, next_service='april')
        url = reverse('truck-detail', kwargs={'pk': new_truck.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_truck_detail_returns_401_status_code_without_authentication(self):
        """
        Ensure that we are not able to get each trucks's details without authentication.
        """
        new_truck = Truck.objects.create(make='Ford', model='Bronco', year=1981, seats=4, bed_length="4 ft", color='orange', VIN='12345671234567abc', current_mileage=19000, service_interval=3, next_service='april')
        self.client.force_authenticate(user=None)
        url = reverse('truck-detail', kwargs={'pk': new_truck.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_create_truck(self):
        """
        Ensure that we are able to create a new truck object.
        """
        url = reverse('truck-list')
        data = {
            'make': 'Ford',
            'model': 'Bronco',
            'year': 1981,
            'seats': 4,
            'bed_length': '4 ft',
            'color': 'orange',
            'VIN': '12345671234567abc',
            'current_mileage': 20000,
            'service_interval': 6,
            'next_service': 'July',
        }
        initial_truck_count = Truck.objects.count()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Truck.objects.count(), initial_truck_count + 1)
        self.assertEqual(Truck.objects.get().make, 'Ford')
    
    def test_create_truck_returns_401_status_code_without_authentication(self):
        """
        Ensure that we are not able to create a new truck object without authentication.
        """
        url = reverse('truck-list')
        data = {
            'make': 'Ford',
            'model': 'Bronco',
            'year': 1981,
            'seats': 4,
            'bed_length': '4 ft',
            'color': 'orange',
            'VIN': '12345671234567abc',
            'current_mileage': 20000,
            'service_interval': 6,
            'next_service': 'July',
        }
        initial_truck_count = Truck.objects.count()
        self.client.force_authenticate(user=None)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Truck.objects.count(), initial_truck_count)
    
    def test_update_truck(self):
        """
        Ensure that we are able to update truck objects.
        """
        new_truck = Truck.objects.create(make='Ford', model='Bronco', year=1981, seats=4, bed_length="4 ft", color='orange', VIN='12345671234567abc', current_mileage=19000, service_interval=3, next_service='april')
        url = reverse('truck-detail', kwargs={'pk': new_truck.pk})
        data = {
            'make': 'test',
            'model': 'test',
            'year': 2014,
            'seats': 4,
            'bed_length': '3 ft',
            'color': 'blue',
            'VIN': '12345671234567abc',
            'current_mileage': 20000,
            'service_interval': 6,
            'next_service': 'July',
        }
        response = self.client.put(url, data=data)
        self.assertEqual(new_truck.make, 'Ford')
        new_truck.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(new_truck.make, 'test')
    
    def test_update_truck_returns_401_status_code_without_authentication(self):
        """
        Ensure that we are not able to update truck objects without authentication.
        """
        new_truck = Truck.objects.create(make='Ford', model='Bronco', year=1981, seats=4, bed_length="4 ft", color='orange', VIN='12345671234567abc', current_mileage=19000, service_interval=3, next_service='april')
        url = reverse('truck-detail', kwargs={'pk': new_truck.pk})
        data = {
            'make': 'test',
            'model': 'test',
            'year': 2014,
            'seats': 4,
            'bed_length': '3 ft',
            'color': 'blue',
            'VIN': '12345671234567abc',
            'current_mileage': 20000,
            'service_interval': 6,
            'next_service': 'July',
        }
        self.assertEqual(new_truck.make, 'Ford')
        self.client.force_authenticate(user=None)
        response = self.client.put(url, data=data)
        new_truck.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(new_truck.make, 'Ford')
    
    def test_delete_truck(self):
        """
        Ensure that we are able to delete a truck object.
        """
        new_truck = Truck.objects.create(make='Ford', model='Bronco', year=1981, seats=4, bed_length="4 ft", color='orange', VIN='12345671234567abc', current_mileage=19000, service_interval=3, next_service='april')
        initial_truck_count = Truck.objects.count()
        url = reverse('truck-detail', kwargs={'pk': new_truck.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Truck.objects.count(), initial_truck_count - 1)
    
    def test_delete_truck_returns_401_status_code_without_authentication(self):
        """
        Ensure that we are not able to delete a truck object without authentication.
        """
        new_truck = Truck.objects.create(make='Ford', model='Bronco', year=1981, seats=4, bed_length="4 ft", color='orange', VIN='12345671234567abc', current_mileage=19000, service_interval=3, next_service='april')
        initial_truck_count = Truck.objects.count()
        url = reverse('truck-detail', kwargs={'pk': new_truck.pk})
        self.client.force_authenticate(user=None)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Truck.objects.count(), initial_truck_count)


class BoatTests(APITestCase):
    def setUp(self):
        self.username = 'admin'
        self.password = 'password123'
        self.user = User.objects.create(username=self.username, password=self.password)
        self.client.force_authenticate(user=self.user)
    
    def test_get_boat_list(self):
        """
        Ensure that we are able to get a readable list of all the boat objects.
        """
        new_boat = Boat.objects.create(make='Bertram', model='28CC', year=2021, length='30 ft', width="7 ft", HIN='12345671234abc', current_hours=40, service_interval=3, next_service='June')
        url = reverse('boat-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Boat.objects.count(), 1)
    
    def test_get_boat_list_returns_401_status_code_without_authentication(self):
        """
        Ensure that we are not able to get a readable list of all the boat objects without authentication.
        """
        new_truck = Boat.objects.create(make='Bertram', model='28CC', year=2021, length='30 ft', width="7 ft", HIN='12345671234abc', current_hours=40, service_interval=3, next_service='June')
        self.client.force_authenticate(user=None)
        url = reverse('boat-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_get_boat_detail(self):
        """
        Ensure that we are able to get each boat's details.
        """
        new_boat = Boat.objects.create(make='Bertram', model='28CC', year=2021, length='30 ft', width="7 ft", HIN='12345671234abc', current_hours=40, service_interval=3, next_service='June')
        url = reverse('boat-detail', kwargs={'pk': new_boat.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_truck_detail_returns_401_status_code_without_authentication(self):
        """
        Ensure that we are not able to get each boat's details without authentication.
        """
        new_boat = Boat.objects.create(make='Bertram', model='28CC', year=2021, length='30 ft', width="7 ft", HIN='12345671234abc', current_hours=40, service_interval=3, next_service='June')
        self.client.force_authenticate(user=None)
        url = reverse('boat-detail', kwargs={'pk': new_boat.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_create_boat(self):
        """
        Ensure that we are able to create a new boat object.
        """
        url = reverse('boat-list')
        data = {
            'make': 'Bertram',
            'model': '28cc',
            'year': 2021,
            'length': '30 ft',
            'width': '7 ft',
            'HIN': '12345671234abc',
            'current_hours': 40,
            'service_interval': 3,
            'next_service': 'June',
        }
        initial_boat_count = Boat.objects.count()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Boat.objects.count(), initial_boat_count + 1)
        self.assertEqual(Boat.objects.get().make, 'Bertram')
    
    def test_create_boat_returns_401_status_code_without_authentication(self):
        """
        Ensure that we are not able to create a new boat object without authentication.
        """
        url = reverse('boat-list')
        data = {
            'make': 'Bertram',
            'model': '28cc',
            'year': 2021,
            'length': '30 ft',
            'width': '7 ft',
            'HIN': '12345671234abc',
            'current_hours': 40,
            'service_interval': 3,
            'next_service': 'June',
        }
        initial_boat_count = Boat.objects.count()
        self.client.force_authenticate(user=None)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Boat.objects.count(), initial_boat_count)
    
    def test_update_boat(self):
        """
        Ensure that we are able to update boat objects.
        """
        new_boat = Boat.objects.create(make='Bertram', model='28CC', year=2021, length='30 ft', width="7 ft", HIN='12345671234abc', current_hours=40, service_interval=3, next_service='June')
        url = reverse('boat-detail', kwargs={'pk': new_boat.pk})
        data = {
            'make': 'Lund',
            'model': '33cc',
            'year': 2021,
            'length': '30 ft',
            'width': '7 ft',
            'HIN': '12345671234abc',
            'current_hours': 40,
            'service_interval': 3,
            'next_service': 'June',
        }
        response = self.client.put(url, data=data)
        self.assertEqual(new_boat.make, 'Bertram')
        new_boat.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(new_boat.make, 'Lund')
    
    def test_update_boat_returns_401_status_code_without_authentication(self):
        """
        Ensure that we are not able to update boat objects without authentication.
        """
        new_boat = Boat.objects.create(make='Bertram', model='28CC', year=2021, length='30 ft', width="7 ft", HIN='12345671234abc', current_hours=40, service_interval=3, next_service='June')
        url = reverse('boat-detail', kwargs={'pk': new_boat.pk})
        data = {
            'make': 'Lund',
            'model': '33cc',
            'year': 2021,
            'length': '30 ft',
            'width': '7 ft',
            'HIN': '12345671234abc',
            'current_hours': 40,
            'service_interval': 3,
            'next_service': 'June',
        }
        self.assertEqual(new_boat.make, 'Bertram')
        self.client.force_authenticate(user=None)
        response = self.client.put(url, data=data)
        new_boat.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(new_boat.make, 'Bertram')
    
    def test_delete_boat(self):
        """
        Ensure that we are able to delete a boat object.
        """
        new_boat = Boat.objects.create(make='Bertram', model='28CC', year=2021, length='30 ft', width="7 ft", HIN='12345671234abc', current_hours=40, service_interval=3, next_service='June')
        initial_boat_count = Boat.objects.count()
        url = reverse('boat-detail', kwargs={'pk': new_boat.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Boat.objects.count(), initial_boat_count - 1)
    
    def test_delete_truck_returns_401_status_code_without_authentication(self):
        """
        Ensure that we are not able to delete a boat object without authentication.
        """
        new_boat = Boat.objects.create(make='Bertram', model='28CC', year=2021, length='30 ft', width="7 ft", HIN='12345671234abc', current_hours=40, service_interval=3, next_service='June')
        initial_boat_count = Boat.objects.count()
        url = reverse('boat-detail', kwargs={'pk': new_boat.pk})
        self.client.force_authenticate(user=None)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Boat.objects.count(), initial_boat_count)