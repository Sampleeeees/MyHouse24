from django.urls import path
from .views import *

urlpatterns = [
    path('', ReceiptList.as_view(), name='ReceiptList'),
    path('create/', ReceiptCreate.as_view(), name='ReceiptCreate'),
    path('update/<int:pk>', ReceiptUpdate.as_view(), name='ReceiptUpdate'),
    path('delete/<int:pk>', ReceiptDelete.as_view(), name='ReceiptDelete'),

    path('receipt_list_dataTable/', receipt_list, name='receipt_list_dataTable'),
    path('filter_house_receipt/', filter_house_receipt, name='filter_house_receipt'),
    path('filter_appartament_receipt/', filter_appartament_receipt, name='filter_appartament_receipt'),
    path('appartament_detail_receipt/', appartament_detail_receipt, name='appartament_detail_receipt'),
    path('delete_selected_receipt/', delete_selected_receipt, name='delete_selected_receipt'),
    path('check_receipt_measure/', check_receipt_measure, name='check_receipt_measure'),
    path('all_service_for_tarrif/', all_service_for_tarrif, name='all_service_for_tarrif'),
    path('add_meter_data/', add_meter_data, name='add_meter_data'),
]