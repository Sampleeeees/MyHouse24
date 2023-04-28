from django.urls import path
from Messages import views

urlpatterns = [
    path('', views.MessagesList.as_view(), name='message_list'),
    path('create_message/', views.MessageCreate.as_view(), name='message_create'),
    path('message_detail/<int:pk>', views.MessageDetail.as_view(), name='message_detail'),
    path('message_delete/<int:pk>', views.MessageDelete.as_view(), name='message_delete'),

    #filter
    path('filter_message', views.filter_message, name='filter_messages'),
    path('filter_message_appartament', views.filter_appartament_message, name='filter_message_appartament')
]