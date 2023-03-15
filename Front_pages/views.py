
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.forms import modelformset_factory, formset_factory
from .models import GeneralPage, SeoBlock, BlockAndServices, AboutUs, Contacts, Document
from .forms import GeneralPageForm, SeoBlockForm, BlockAndServicesForm, AboutUsForm, DocumentForm, ContactsForm
from django.views.generic import UpdateView, View, CreateView
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


    def get_context_data(self, **kwargs):
        context = super(GeneralUpdate, self).get_context_data(**kwargs)
        return context
class AboutUsUpdate(UpdateView):
    model = AboutUs
    template_name = 'Front_pages/aboutUsUpdate.html'
    form_class = AboutUsForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ImageFormset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)
        DocumentFormset = modelformset_factory(Document, form=DocumentForm, extra=0, can_delete=True)
        context['aboutUsOther'] = AboutUs.objects.get(pk=3)
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

