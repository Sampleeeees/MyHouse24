from django.urls import path
from .views import *
urlpatterns = [
    path('', GeneralDetail.as_view(), name='FrontGeneral'),
    path('about_us/', AboutUsView.as_view(), name='AboutUsView'),
    path('services/', ServicesView.as_view(), name='ServicesView'),
    path('contacts/', ContactView.as_view(), name='ContactView'),
]