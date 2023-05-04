from django.urls import path

from Meters_data.views import *

urlpatterns = [
    path('', MeterDataList.as_view(), name='Meter_data_list'),
    path('create_meter_data/', MeterDataCreate, name='Meter_data_create'),
    path('history_meter_data/<int:pk>', MeterDataDetail, name='Meter_data_history'),
    path('filter_house_meter/', filter_house_meter, name='filter_house_meter'),
    path('json/dataTable/meter_data/', meter_data_list, name='meter_data_list')
]