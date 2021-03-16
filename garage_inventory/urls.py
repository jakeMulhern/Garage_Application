from django.urls import path, include
from .views import CarViewSet, TruckViewSet, BoatViewSet, api_root, UserViewSet
from rest_framework import renderers
from rest_framework.authtoken import views

car_list = CarViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
car_detail = CarViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy', 
})
truck_list = TruckViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
truck_detail = TruckViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})
boat_list = BoatViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
boat_detail = BoatViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('', api_root),
    path('cars/', car_list, name='car-list'),
    path('cars/<int:pk>/', car_detail, name='car-detail'),
    path('trucks/', truck_list, name='truck-list'),
    path('trucks/<int:pk>/', truck_detail, name='truck-detail'),
    path('boats/', boat_list, name='boat-list'),
    path('boats/<int:pk>/', boat_detail, name='boat-detail'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>', user_detail, name='user-detail'),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]