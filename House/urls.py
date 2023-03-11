from django.urls import path
from .views import HouseList, HouseCreate, HouseUpdate

urlpatterns = [
    path('', HouseList.as_view(), name='house_list'),
    path('create/', HouseCreate.as_view(), name='house_create'),
    path('update/<int:pk>', HouseUpdate.as_view(), name='house_update')
]