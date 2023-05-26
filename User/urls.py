from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_request, name='register_view'),
    path('login_owner/', views.login_request, name='login_view'),
    path('login_admin/', views.login_request_admin, name='login_admin'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('logout/', views.logout_request, name='logout'),
]