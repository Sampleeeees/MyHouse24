from django.urls import path
from . import views

urlpatterns = [
    path('', views.BaseView.as_view(), name='base_admin'),
    path('statistics/', views.Statistic, name='statistic'),
    path('appartaments/', views.AppartamentList.as_view(), name='appartament_list'),
    path('appartament/detail/<int:pk>', views.AppartamentDetail.as_view(), name='appartament_detail'),
    path('appartament/create', views.AppartamentCreate.as_view(), name='appartament_create'),
    path('appartament/delete/<int:pk>', views.AppartamentDelete.as_view(), name='appartament_delete'),
    path('appartament/update/<int:pk>', views.AppartamentUpdate.as_view(), name='appartament_update'),
    path('owner_appartaments', views.OwnerAppartamentsList.as_view(), name="ownerAppartamentsList"),
    path('owner_appartament/create_owner', views.AddOwnerAppartamentCreate.as_view(), name="add_owner_appartament"),
    path('onwer_appartament/send_invite', views.SendInviteOwnerAppartament.as_view(), name='send_invite_owner'),
    path('onwer_appartament/send_invite_email/<int:pk>', views.SendEmailInviteOwnerAppartament.as_view(), name='send_invite_email_owner'),
    path('owner_appartament/delete/<int:pk>', views.OwnerAppartamentDelete.as_view(), name='owner_appartament_delete'),
    path('owner_appartament/update/<int:pk>', views.OwnerAppartamentUpdate.as_view(), name='owner_appartament_update'),
    path('json/dataTable/owner_appartaments', views.owner_appartament_list, name='owner_appartament_dataTable'),
    path('json/dataTable/appartament_list', views.appartament_list, name='appartament_list_dataTable'),

    #filter
    path('filter_house', views.filter_house, name="filter_house")
]