import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import modelformset_factory
from django.template.loader import render_to_string, get_template


def base(request):
    return render(request, 'Front_pages/base.html')
# Create your views here.
