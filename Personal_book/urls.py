from django.urls import path
from Personal_book.views import *

urlpatterns = [
    path('', PersonalList.as_view(), name='PersonalList'),
    path('create/', PersonalCreate.as_view(), name='PersonalCreate'),
    path('update/<int:pk>', PersonalUpdate.as_view(), name='PersonalUpdate'),
    path('delete/<int:pk>', PersonalDelete.as_view(), name='PersonalDelete'),
    path('export-to-excel/', export_to_excel, name='export_to_excel'),

    path('json/dataTable/personal_list', personal_book_list, name='personal_book_list'),
    path('filter_house_personal', filter_house_personal, name='filter_house_personal'),
    path('filter_appartament_personal', filter_appartament_personal, name='filter_appartament_personal'),
    path('appartament_detail', appartament_detail, name='personal_appartament_detail'),
]