import datetime
import datetime
from django.utils import timezone
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Message
from .forms import MessageForm
from django.views.generic import UpdateView, CreateView, DeleteView, DetailView, ListView
import json
from django.core.serializers import serialize
from House.models import House, Section, Floor
from Appartament.models import Appartament
from User.models import User
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
UserModel = get_user_model()

# Create your views here.
class MessagesList(ListView):
    model = Message
    template_name = 'Messages/message_list.html'
    queryset = Message.objects.all()


class MessageCreate(CreateView):
    model = Message
    template_name = 'Messages/message_create.html'
    form_class = MessageForm
    success_url = reverse_lazy('message_list')

    def form_valid(self, form):
        users = User.objects.filter(appartament=form.instance.appartament.id)

        form.instance.date_send = timezone.now()
        form.instance.user_send = self.request.user.get_full_name()

        print(form.cleaned_data)

        for user in users:
            current_site = get_current_site(self.request)
            mail_subject = f'Від MyHouse24:{form.instance.title_mess}'
            message = render_to_string('Messages/send_message_to_email.html', {
                'form': form,
                'domain': current_site.domain,
            })
            to_email = user.email
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            print('Sending')
        return super().form_valid(form=form)


class MessageDetail(DetailView):
    model = Message
    template_name = 'Messages/message_detail.html'


class MessageDelete(DeleteView):
    model = Message
    success_url = reverse_lazy('message_list')

    def get(self, request, *args, **kwargs):
        return self.delete(self, request, *args, **kwargs)


def filter_message(request):
    if request.GET.get('house_id') != '' and request.GET.get('house_id') is not None:
        print(request.GET.get('section_id'))
        sections = serialize('json', Section.objects.filter(house_id=request.GET.get('house_id')))
        floors = serialize('json', Floor.objects.filter(house_id=request.GET.get('house_id')))
        return JsonResponse({'sections': sections, 'floors': floors}, status=200)
    else:
        print('Hallo')
        return JsonResponse({'sections': 0, 'floors': 0}, status=200)

def filter_appartament_message(request):
    print(request.GET.get('house_id'), request.GET.get('section_id'), request.GET.get('floor_id'))
    if request.GET.get('house_id') != '' and request.GET.get('section_id') != '' and request.GET.get('floor_id') != '':
        appartaments = serialize('json', Appartament.objects.filter(house_id=request.GET.get('house_id'), section_id=request.GET.get('section_id'), floor_id=request.GET.get('floor_id')))
        return JsonResponse({'appartaments': appartaments}, status=200)
    else:
        return JsonResponse({'appartaments': 0}, status=200)

