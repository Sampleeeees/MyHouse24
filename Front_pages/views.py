import json

import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import GeneralPage, SeoBlock, BlockAndServices
from .forms import GeneralPageForm, SeoBlockForm, BlockAndServicesForm
from django.views.generic import UpdateView, View, CreateView


def base(request):
    return render(request, 'Front_pages/base.html')
# Create your views here.

class GeneralUpdate(UpdateView):
    model = GeneralPage
    template_name = 'Front_pages/generalpage_detail.html'
    form_class = GeneralPageForm
    def get_context_data(self, **kwargs):
        context = super(GeneralUpdate, self).get_context_data(**kwargs)
        seoinstance = SeoBlock.objects.get(pk=GeneralUpdate.get_object(self).seo.pk)
        blocks = BlockAndServices.objects.filter(pk=GeneralUpdate.get_object(self).block.pk)
        context['blocks'] = blocks
        for item in blocks:
            context['blockarea'] = BlockAndServicesForm(instance=item)
        context['seo'] = SeoBlockForm(instance=seoinstance)
        return context

