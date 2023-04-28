from django.urls import path
from Master_application import views

urlpatterns = [
    path('', views.MasterList.as_view(), name='master_list'),
    path('create_appliaction/', views.MasterCreate.as_view(), name='master_create'),

    path('json/dataTable/master_list', views.master_appartament_list, name='master_appartaments_list'),
    path('filter_master_appartament/', views.filter_master_appartament, name='filter_master_appartament'),
]