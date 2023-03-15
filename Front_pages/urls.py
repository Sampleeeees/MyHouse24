from django.urls import path
from . import views

urlpatterns = [
    path('general_page/<int:pk>', views.GeneralUpdate.as_view(), name='general_page'),
    path('about_us/<int:pk>', views.AboutUsUpdate.as_view(), name='aboutUs'),
    path('contacts/<int:pk>', views.ContactsUpdate.as_view(), name='contacts')
]