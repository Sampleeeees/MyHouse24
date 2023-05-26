from django.urls import path
from .views import *

urlpatterns = [
    path('', StatementList.as_view(), name='StatementList'),
    path('create_plus/', StatementCreatePlus.as_view(), name='StatementCreatePlus'),
    path('create_minus/', StatementCreateMinus.as_view(), name='StatementCreateMinus'),
    path('delete/<int:pk>', StatementDelete.as_view(), name='StatementDelete'),
    path('update_plus/<int:pk>', StatementUpdatePlus.as_view(), name='StatementUpdatePlus'),
    path('update_minus/<int:pk>', StatementUpdateMinus.as_view(), name='StatementUpdateMinus'),

    path('json/dataTable/statement', statement_list, name='statement_list_dataTable')
]