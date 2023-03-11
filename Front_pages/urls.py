from django.urls import path
from . import views

urlpatterns = [
    path('general_page/<int:pk>', views.GeneralUpdate.as_view(), name='general_page')
]