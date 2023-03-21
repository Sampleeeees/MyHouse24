from django.urls import path
from . import views

urlpatterns = [
    path('general_page/', views.GeneralUpdate.as_view(), name='general_page'),
    path('about_us/', views.AboutUsUpdate.as_view(), name='aboutUs'),
    path('aboutus/deleteimage/<int:pk>', views.ImageDelete.as_view(), name='delete-image'),
    path('aboutus/deletedocument/<int:pk>', views.DocumentDelete.as_view(), name='delete-document'),
    path('contacts/', views.ContactsUpdate.as_view(), name='contacts'),
    path('services/', views.ServicesUpdate.as_view(), name='services'),
    path('services/delete_service/<int:pk>', views.ServiceDelete.as_view(), name='delete-service'),
    path('tarrif/', views.PageTarrifUpdate.as_view(), name='pageTarrif')
]