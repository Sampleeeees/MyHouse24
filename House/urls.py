from django.urls import path
from .views import HouseList, HouseCreate, HouseUpdate, delete_item, HouseDetail, house_list

urlpatterns = [
    path('', HouseList.as_view(), name='house_list'),
    path('create/', HouseCreate.as_view(), name='house_create'),
    path('update/<int:pk>', HouseUpdate.as_view(), name='house_update'),
    path('delete/<int:pk>', delete_item, name='house_delete'),
    path('detail/<int:pk>', HouseDetail.as_view(), name='house_detail'),
    path('json/dataTables/House', house_list, name='dataTableHouse')
]