from django.urls import path
from Master_application import views

urlpatterns = [
    path('', views.MasterList.as_view(), name='master_list'),
    path('create_appliaction/', views.MasterCreate.as_view(), name='master_create'),
    path('update_application/<int:pk>', views.MasterUpdate.as_view(), name='master_update'),
    path('detail_application/<int:pk>', views.MasterDetail.as_view(), name='master_detail'),
    path('delete_application/<int:pk>', views.MasterDelete.as_view(), name='master_delete'),

    path('json/dataTable/master_list', views.master_appartament_list, name='master_appartaments_list'),
    path('filter_master_appartament/', views.filter_master_appartament, name='filter_master_appartament'),
]