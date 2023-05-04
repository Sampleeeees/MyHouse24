from django.urls import path
from Personal_book.views import *

urlpatterns = [
    path('', PersonalList.as_view(), name='PersonalList'),

    path('json/dataTable/personal_list', personal_book_list, name='personal_book_list'),
    path('filter_house_personal', filter_house_personal, name='filter_house_personal')
]