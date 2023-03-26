from django.urls import path
from . import views

urlpatterns = [
    path('service/', views.SettingServiceUpdate.as_view(), name='setting_service'),
    path('payment/', views.PaymentUpdate.as_view(), name='paymentUpdate'),
    path('tarrif', views.TarrifList.as_view(), name='tarrifList'),
    path('tarrif/create', views.TarrifCreate.as_view(), name='tarrifCreate'),
    path('measure/delete/<int:pk>', views.MeasureDelete.as_view(), name='measureDelete'),
    path('service/delete/<int:pk>', views.ServiceDelete.as_view(), name='serviceDelete'),
    path('check_measure', views.check_measure, name='checkMeasure')

]