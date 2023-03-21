from django.shortcuts import render
from django.views.generic import View
from Front_pages.models import *
# Create your views here.

class BaseView(View):
    def get(self, request):
        general = GeneralPage.objects.first()
        contact = Contacts.objects.first()

        return render(request, 'Appartament/base.html')