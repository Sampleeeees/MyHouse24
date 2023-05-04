from django.core.paginator import Paginator
from django.core.serializers import serialize
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from Personal_book.models import *
# Create your views here.

class PersonalList(ListView):
    model = PersonalBook
    template_name = 'Personal_book/personal_list.html'
    queryset = PersonalBook.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PersonalList, self).get_context_data(**kwargs)
        context['houses'] = House.objects.all()
        context['owners'] = User.objects.filter(appartament__isnull=False).distinct()
        context['all_book'] = PersonalBook.objects.all().count()
        return context


class PersonalCreate(CreateView):
    model = PersonalBook
    template_name = 'Personal_book/personal_create.html'


def personal_book_list(request):
    personals = PersonalBook.objects.all()

    #Search
    search_personal_num = request.GET.get('personal_num')
    search_personal_status = request.GET.get('personal_status')
    search_personal_flat = request.GET.get('personal_flat')
    search_personal_house = request.GET.get('personal_house')
    search_personal_section = request.GET.get('personal_section')
    search_personal_owner = request.GET.get('personal_owner')
    search_personal_residual = request.GET.get('personal_residual')

    query = Q()

    if search_personal_num:
        query &= Q(id__icontains=search_personal_num)

    if search_personal_status:
        query &= Q(status=search_personal_status)

    if search_personal_flat:
        query &= Q(appartament__number_appartament__icontains=search_personal_flat)

    if search_personal_house:
        query &= Q(house_id=search_personal_house)

    if search_personal_section:
        query &= Q(section_id=search_personal_section)

    if search_personal_owner:
        query &= Q(owner_id=search_personal_owner)

    if search_personal_residual:
        query &= Q(residual__icontains=search_personal_residual)

    personals = personals.filter(query)

    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))

    paginator = Paginator(personals, length)
    personals = paginator.get_page(start // length + 1)

    data = []

    for personal in personals:
        data.append({
            'num': personal.id,
            'status': personal.get_status_display(),
            'flat': personal.appartament.number_appartament,
            'house': personal.house.name_home,
            'section': personal.section.name_section,
            'owner': personal.owner.get_full_name(),
            'residual': personal.residual
        })

    response = {
        'draw': request.GET.get('draw'),
        'recordsTotal': PersonalBook.objects.all().count(),
        'recordsFiltered': personals.paginator.count,
        'data': data
    }

    return JsonResponse(response)


def filter_house_personal(request):
    print(request.GET.get('house_id'))
    if request.GET.get('house_id') != '' and request.GET.get('house_id') is not None:
        print('Hello')
        sections = serialize('json', Section.objects.filter(house_id=request.GET.get('house_id')))
        return JsonResponse({'sections': sections}, status=200)
    else:
        print('Not Working')
        return JsonResponse({}, status=200)
