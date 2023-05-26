from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
from Front_pages.models import *
from Gallery.models import Image, Gallery
# Create your views here.
class GeneralDetail(TemplateView):
    model = GeneralPage
    template_name = 'pages/front_general.html'

    def get_context_data(self, **kwargs):
        context = super(GeneralDetail, self).get_context_data(**kwargs)
        context['general'] = GeneralPage.objects.first()
        context['services'] = BlockAndServices.objects.filter(generalPage=context['general'])
        context['contact'] = Contacts.objects.first()
        return context


class AboutUsView(TemplateView):
    model = Contacts
    template_name = 'pages/front_about_us.html'


    def get_context_data(self, **kwargs):
        context = super(AboutUsView, self).get_context_data(**kwargs)
        context['about'] = AboutUs.objects.first()
        context['images'] = Image.objects.filter(gallery_id=context['about'].gallery.id)
        context['documents'] = Document.objects.all()
        return context

class ServicesView(TemplateView):
    model = Services
    template_name = 'pages/front_services.html'

class ContactView(TemplateView):
    model = Contacts
    template_name = 'pages/front_contacts.html'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['contact'] = Contacts.objects.first()
        return context
