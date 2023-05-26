from django.urls import path

from Meters_data.views import *

urlpatterns = [
    path('', MeterDataList.as_view(), name='Meter_data_list'),
    path('create_meter_data/', MeterDataCreate.as_view(), name='Meter_data_create'),
    path('copy_meter_data/<int:pk>', MeterDataCopy.as_view(), name='Meter_data_copy'),
    path('delete/<int:pk>', MeterDataDelete.as_view(), name='Meter_data_delete'),
    path('update/<int:pk>', MeterDataUpdate.as_view(), name='Meter_data_update'),
    path('meter_sort_data/', MeterDataSortList.as_view(), name='meter_sort_data'),
    path('filter_house_meter/', filter_house_meter, name='filter_house_meter'),
    path('json/dataTable/meter_data/', meter_data_list, name='meter_data_list'),
    path('json/dataTable/meter_data_sort/', meter_sort_data, name='meter_data_sort')
]