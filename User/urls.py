from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoginViews.as_view(), name='login_view')
]