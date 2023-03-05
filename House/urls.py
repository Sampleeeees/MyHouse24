from django.urls import path
from .views import HouseList, HouseCreate

urlpatterns = [
    path('', HouseList.as_view(), name='house_list'),
    path('create/', HouseCreate.as_view(), name='house_create')
]