from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.core.serializers import serialize
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .models import MatsterApplication
from .forms import MasterForm
from Appartament.models import Appartament
from House.models import House
from User.models import User
# Create your views here.

class MasterList(ListView):
    model = MatsterApplication
    template_name = 'Master_application/master_list.html'
    queryset = MatsterApplication.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MasterList, self).get_context_data(**kwargs)
        context['owners'] = User.objects.all()
        context['masters'] = User.objects.filter(role__user__isnull=False)
        return context

class MasterCreate(CreateView):
    form_class = MasterForm
    template_name = 'Master_application/master_create.html'
    success_url = reverse_lazy('master_list')

    def get_context_data(self, **kwargs):
        context = super(MasterCreate, self).get_context_data(**kwargs)
        return context

class MasterUpdate(UpdateView):
    form_class = MasterForm
    model = MatsterApplication
    template_name = 'Master_application/master_update.html'
    success_url = reverse_lazy('master_list')

    def get_context_data(self, **kwargs):
        context = super(MasterUpdate, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        return super().form_valid(form=form)

class MasterDetail(DetailView):
    model = MatsterApplication
    template_name = 'Master_application/master_detail.html'

class MasterDelete(DeleteView):
    model = MatsterApplication
    success_url = reverse_lazy('master_list')

    def get(self, request, *args, **kwags):
        return self.delete(self, request, *args, *kwags)

def filter_master_appartament(request):
    print(request.GET.get('owner_id'))
    if request.GET.get('owner_id') != '' or request.GET.get('owner_id') is not None:
        appartaments = serialize('json', Appartament.objects.filter(owner_id=request.GET.get('owner_id')))
        houses = serialize('json', House.objects.all())
        return JsonResponse({'appartaments': appartaments, 'houses': houses}, status=200)


def master_appartament_list(request):
    masters = MatsterApplication.objects.all()

    #Search
    search_master_num = request.GET.get('master_num')
    search_master_time = request.GET.get('master_time')
    search_master_type = request.GET.get('master_type')
    search_master_description = request.GET.get('master_description')
    search_master_flat = request.GET.get('master_flat')
    search_master_owner = request.GET.get('master_owner')
    search_master_phone = request.GET.get('master_phone')
    search_master_name = request.GET.get('master_name')
    search_master_status = request.GET.get('master_status')

    query = Q()


    if search_master_num:
        query &= Q(id__icontains=search_master_num)

    if search_master_time:
        query &= Q(Q(date_master__icontains=search_master_time) | Q(time_master__icontains=search_master_time))

    if search_master_type:
        query &= Q(typeMaster__name=search_master_type)

    if search_master_description:
        query &= Q(description_problem__icontains=search_master_description)

    if search_master_flat:
        query &= Q(appartament__number_appartament__icontains=search_master_flat)

    if search_master_owner:
        query &= Q(ownerAppartament=search_master_owner)

    if search_master_phone:
        query &= Q(name_master__phone_number__icontains=search_master_phone)

    if search_master_name:
        query &= Q(name_master_id=search_master_name)

    if search_master_status:
        query &= Q(status=search_master_status)

    masters = masters.filter(query)

    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))

    paginator = Paginator(masters, length)
    masters = paginator.get_page(start // length + 1)

    data = []

    for master in masters:
        data.append({
            'id': master.id,
            'time': master.time_master,
            'type': master.typeMaster.name,
            'description': master.description_problem,
            'flat': master.appartament.number_appartament,
            'owner': master.ownerAppartament.get_full_name(),
            'phone': master.name_master.phone_number,
            'master': master.name_master.get_full_name(),
            'status': master.status
        })

    response = {
        'draw': request.GET.get('draw'),
        'recordsTotal': MatsterApplication.objects.all().count(),
        'recordsFiltered': masters.paginator.count,
        'data': data
    }

    return JsonResponse(response)