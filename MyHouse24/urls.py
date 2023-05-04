"""MyHouse24 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('adminer/', admin.site.urls),
    path('admin/pages/', include('Front_pages.urls')),
    path('admin/', include('Appartament.urls')),
    path('user/', include('User.urls')),
    path('admin/house/', include('House.urls')),
    path('admin/setting/', include('Tarrif_and_services.urls')),
    path('admin/messages/', include('Messages.urls')),
    path('admin/master_appliactions/', include('Master_application.urls')),
    path('admin/meter_data/', include('Meters_data.urls')),
    path('admin/personal_book', include('Personal_book.urls'))
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)