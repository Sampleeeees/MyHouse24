from django.urls import path
from . import views

urlpatterns = [
    path('service/', views.SettingServiceUpdate.as_view(), name='setting_service'),
    path('payment/', views.PaymentUpdate.as_view(), name='paymentUpdate'),
    path('tarrif', views.TarrifList.as_view(), name='tarrifList'),
    path('tarrif/create', views.TarrifCreate.as_view(), name='tarrifCreate'),
    path('tarrif/detail/<int:pk>', views.TarrifDetail.as_view(), name='tarrifDetail'),
    path('tarrif/update/<int:pk>', views.TarrifUpdate.as_view(), name='tarrifUpdate'),
    path('tarrif/delete/<int:pk>', views.TarrifDelete.as_view(), name='tarrifDelete'),
    path('measure/delete/<int:pk>', views.MeasureDelete.as_view(), name='measureDelete'),
    path('service/delete/<int:pk>', views.ServiceDelete.as_view(), name='serviceDelete'),
    path('check_measure', views.check_measure, name='checkMeasure'),
    path('article/', views.ArticleList.as_view(), name='articleList'),
    path('article/create', views.ArticleCreate.as_view(), name='articleCreate'),
    path('article/update/<int:pk>', views.ArticleUpdate.as_view(), name='articleUpdate'),
    path('article/delete/<int:pk>', views.ArticleDelete.as_view(), name='articleDelete'),
    path('users/', views.UsersList.as_view(), name='usersList'),
    path('user/detail/<int:pk>', views.UserDetail.as_view(), name='userDetail'),
    path('user/update/<int:pk>', views.UserUpdate.as_view(), name='userUpdate'),
    path('user/delete/<int:pk>', views.UserDelete.as_view(), name='userDelete'),
    path('user/create', views.UserCreate.as_view(), name='userCreate'),
    path('user/send_invite/<user_id>', views.UserSend.as_view(), name='send_invite_to_email')

]