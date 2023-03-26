
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.forms import modelformset_factory, formset_factory
from .models import GeneralPage, SeoBlock, BlockAndServices, AboutUs, Contacts, Document, Services, PageTarrif, TarrifForm
from .forms import GeneralPageForm, SeoBlockForm, BlockAndServicesForm, AboutUsForm, DocumentForm, ContactsForm, ServicesForm, TarrifFormForm, PageTarrifForm
from django.views.generic import UpdateView, View, CreateView, DeleteView
from Gallery.models import Image, Gallery
from Gallery.forms import ImageForm, GalleryForm


def base(request):
    return render(request, 'Front_pages/base.html')
# Create your views here.

class GeneralUpdate(UpdateView):
    model = GeneralPage
    template_name = 'Front_pages/generalpage_detail.html'
    form_class = GeneralPageForm
    success_url = reverse_lazy('general_page')

    def get_object(self, queryset=None):
        return GeneralPage.objects.first()

    def get_context_data(self, **kwargs):
        context = super(GeneralUpdate, self).get_context_data(**kwargs)
        print(context)
        BlockFormset = modelformset_factory(BlockAndServices, form=BlockAndServicesForm, extra=0, can_delete=True)
        if self.request.POST:
            context['formset_block'] = BlockFormset(self.request.POST, self.request.FILES, prefix='block', queryset=BlockAndServices.objects.filter(generalPage=context['generalpage'].id))
            context['seo'] = SeoBlockForm(self.request.POST, instance=context['generalpage'].seo)
        else:
            context['formset_block'] = BlockFormset(prefix='block', queryset=BlockAndServices.objects.filter(generalPage=context['generalpage'].id))
            context['seo'] = SeoBlockForm(instance=context['generalpage'].seo)
        return context



    def form_valid(self, form, **kwargs):
        print('545456')
        context = self.get_context_data(form=form, **kwargs)
        print('--*-*-*-*', context)
        form.save()
        context['seo'].save()
        if context['formset_block'].is_valid():
            for block in context['formset_block']:
                bl = block.save(commit=False)
                bl.generalPage_id = context['generalpage'].id
                bl.save()
            context['formset_block'].save()
        return super().form_valid(form)


class AboutUsUpdate(UpdateView):
    model = AboutUs
    template_name = 'Front_pages/aboutUsUpdate.html'
    form_class = AboutUsForm

    def get_object(self, queryset=None):
        return AboutUs.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ImageFormset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)
        DocumentFormset = modelformset_factory(Document, form=DocumentForm, extra=0, can_delete=True)
        context['aboutUsOther'] = AboutUs.objects.get(pk=5)
        if self.request.POST:
            context['formset_image'] = ImageFormset(self.request.POST, self.request.FILES, prefix='general', queryset=Image.objects.filter(gallery=context['aboutus'].gallery.id))
            context['formset_image2'] = ImageFormset(self.request.POST, self.request.FILES, prefix='extra', queryset=Image.objects.filter(gallery=context['aboutUsOther'].gallery.id))
            context['seo'] = SeoBlockForm(self.request.POST, instance=context['aboutus'].seo)
            context['formset_document'] = DocumentFormset(self.request.POST, self.request.FILES, prefix='document', queryset=Document.objects.filter(page=context['aboutus'].id))
        else:
            context['formset_image'] = ImageFormset(prefix='general', queryset=Image.objects.filter(gallery=context['aboutus'].gallery.id))
            context['formset_image2'] = ImageFormset(prefix='extra', queryset=Image.objects.filter(gallery=context['aboutUsOther'].gallery.id))
            context['seo'] = SeoBlockForm(instance=context['aboutus'].seo)
            context['formset_document'] = DocumentFormset(prefix='document', queryset=Document.objects.filter(page=context['aboutus'].id))
        return context

    def form_valid(self, form, **kwargs):
        context = self.get_context_data(form=form, **kwargs)
        context['aboutus'].save()
        context['aboutus'].seo.save()
        context['seo'].save()
        print(context['formset_document'].__dict__)
        if context['formset_image'].is_valid() and context['formset_image2'].is_valid() and context['formset_document']:
            for img1 in context['formset_image']:
                img = img1.save(commit=False)
                img.gallery_id = context['aboutus'].gallery.id
                img.save()
            context['formset_image'].save()
            for img2 in context['formset_image2']:
                img = img2.save(commit=False)
                img.gallery_id = context['aboutUsOther'].gallery.id
                img.save()
            context['formset_image2'].save()
            for document in context['formset_document']:
                doc = document.save(commit=False)
                doc.page_id = context['aboutus'].id
                doc.save()
            context['formset_document'].save()
        else:
            print('No working')
            print(context['formset_document'].error)
        return super().form_valid(form)



class ContactsUpdate(UpdateView):
    model = Contacts
    template_name = 'Front_pages/contacts_detail.html'
    form_class = ContactsForm

    def get_object(self, queryset=None):
        return Contacts.objects.first()

    def get_context_data(self, **kwargs):
        context = super(ContactsUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            context['seo'] = SeoBlockForm(self.request.POST, instance=SeoBlock.objects.get(pk=context['contacts'].seo.id))
        else:
            context['seo'] = SeoBlockForm(instance=SeoBlock.objects.get(pk=context['contacts'].seo.id))
        return context

    def form_valid(self, form, **kwargs):
        context = self.get_context_data(form=form, **kwargs)
        context['contacts'].save()
        context['seo'].save()
        return super().form_valid(form)

class ServicesUpdate(UpdateView):
    model = Services
    template_name = 'Front_pages/services_detail.html'
    form_class = ServicesForm

    def get_object(self, queryset=None):
        return Services.objects.first()

    def get_context_data(self, **kwargs):
        context = super(ServicesUpdate, self).get_context_data(**kwargs)
        ServiceFormset = modelformset_factory(BlockAndServices, form=BlockAndServicesForm, extra=0, can_delete=True)
        if self.request.POST:
            context['seo'] = SeoBlockForm(self.request.POST, instance=context['services'].seo)
            context['formset_service'] = ServiceFormset(self.request.POST, self.request.FILES, prefix='service', queryset=BlockAndServices.objects.filter(services=context['services'].id))
        else:
            context['seo'] = SeoBlockForm(instance=context['services'].seo)
            context['formset_service'] = ServiceFormset(prefix='service', queryset=BlockAndServices.objects.filter(services=context['services'].id))

        return context

    def form_valid(self, form, **kwargs):
        context = self.get_context_data(form=form, **kwargs)
        context['services'].save()
        context['seo'].save()
        for service in context['formset_service']:
            ser = service.save(commit=False)
            ser.services_id = context['services'].id
            ser.save()
        context['formset_service'].save()
        return super().form_valid(form)
    
    
class PageTarrifUpdate(UpdateView):
    model = PageTarrif
    template_name = 'Front_pages/tarrif_detail.html'
    form_class = PageTarrifForm
    
    def get_object(self, queryset=None):
        return PageTarrif.objects.first()
    
    def get_context_data(self, **kwargs):
        context = super(PageTarrifUpdate, self).get_context_data(**kwargs)
        TarrifFormset = modelformset_factory(TarrifForm, form=TarrifFormForm, extra=0, can_delete=True)
        if self.request.POST:
            context['formset_tarrif'] = TarrifFormset(self.request.POST, self.request.FILES, prefix='tarrif', queryset=TarrifForm.objects.filter(pageTarrif=context['object'].id))
            context['seo'] = SeoBlockForm(self.request.POST, instance=context['object'].seo)
        else:
            context['formset_tarrif'] = TarrifFormset(prefix='tarrif', queryset=TarrifForm.objects.filter(pageTarrif=context['object'].id))
            context['seo'] = SeoBlockForm(instance=context['object'].seo)
        return context
    
    def form_valid(self, form):
        context = self.get_context_data(form=form)
        context['object'].save()
        context['seo'].save()
        if context['formset_tarrif'].is_valid():
            for tarrif in context['formset_tarrif']:
                tar = tarrif.save(commit=False)
                tar.pageTarrif_id = context['object'].id
                tar.save()
            context['formset_tarrif'].save()
        return super().form_valid(form=form)
    
class ImageDelete(DeleteView):
    model = Image
    success_url = reverse_lazy('aboutUs')
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

class DocumentDelete(DeleteView):
    model = Document
    success_url = reverse_lazy('aboutUs')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

class ServiceDelete(DeleteView):
    model = BlockAndServices
    success_url = 'admin/pages/services/1'
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, *kwargs)

class TarrifDelete(DeleteView):
    model = TarrifForm
    success_url = reverse_lazy('pageTarrif')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
