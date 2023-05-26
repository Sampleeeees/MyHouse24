from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DetailView, DeleteView, CreateView
from .models import Statement
from django.db.models import Q
from User.models import User
from Articles_and_detail_payments.models import Article
from .forms import StatementForm
from Receipt.models import Receipt
from Tarrif_and_services.models import ServiceforTariif
from Appartament.models import Appartament
# Create your views here.


class StatementList(ListView):
    model = Statement
    template_name = 'Statement/statement_list.html'
    queryset = Statement.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(StatementList, self).get_context_data(**kwargs)
        context['owners'] = User.objects.filter(appartament__isnull=False).distinct()
        context['articles'] = Article.objects.all()

        plus = Statement.objects.filter(amount__gt=0)
        total_plus = 0
        for stat_plus in plus:
            total_plus += stat_plus.amount

        minus = Statement.objects.filter(amount__lt=0)
        total_minus = 0
        for stat_minus in minus:
            total_minus -= stat_minus.amount

        receipts = Receipt.objects.all()
        total_receipt = 0
        for receipt in receipts:
            services = ServiceforTariif.objects.filter(tarrif_id=receipt.tarrif.id)
            for cina in services:
                total_receipt += cina.price * cina.consum

        flat_total = 0
        for flat in Appartament.objects.all():
            try:
                stat = Statement.objects.get(ownerAppartemnt=flat.owner.id, personal_book__appartament_id=flat.id)
                flat_total += stat.amount
            except Statement.DoesNotExist:
                flat_total += 0

        context['flat_total'] = flat_total
        context['total_plus'] = total_plus
        context['total_minus'] = -total_minus
        context['total'] = total_plus - total_minus
        context['total_receipt'] = total_receipt

        return context


class StatementCreatePlus(CreateView):
    model = Statement
    template_name = 'Statement/statement_create_plus.html'
    form_class = StatementForm
    success_url = reverse_lazy('StatementList')

    def form_valid(self, form):
        statement = form.save(commit=False)
        statement.type = 'Прихід'
        statement.save()
        return super().form_valid(form=form)
class StatementCreateMinus(CreateView):
    model = Statement
    template_name = 'Statement/statement_create_minus.html'
    form_class = StatementForm
    success_url = reverse_lazy('StatementList')

    def form_valid(self, form):
        statement = form.save(commit=False)
        statement.type = 'Розхід'
        statement.amount = -1 * statement.amount
        statement.save()
        return super().form_valid(form=form)

class StatementUpdatePlus(UpdateView):
    model = Statement
    template_name = 'Statement/statement_update_plus.html'
    form_class = StatementForm
    success_url = reverse_lazy('StatementList')

class StatementUpdateMinus(UpdateView):
    model = Statement
    template_name = 'Statement/statement_update_minus.html'
    form_class = StatementForm
    success_url = reverse_lazy('StatementList')



class StatementDelete(DeleteView):
    model = Statement
    success_url = reverse_lazy('StatementList')

    def get(self, request, *args, **kwargs):
        return self.delete(self, request, *args, **kwargs)



def statement_list(request):
    statements = Statement.objects.all()

    #SEARCH
    search_statement_num = request.GET.get('statement_num')
    search_statement_date = request.GET.get('statement_date')
    search_statement_status = request.GET.get('statement_status')
    search_statement_type = request.GET.get('statement_type')
    search_statement_owner = request.GET.get('statement_owner')
    search_statement_personal = request.GET.get('statement_personal')
    search_statement_check = request.GET.get('statement_check')

    query = Q()

    if search_statement_num:
        query = Q(uid__icontains=search_statement_num)

    if search_statement_date:
        query = Q(date_published=search_statement_date)

    if search_statement_status:
        query = Q(status=search_statement_status)

    if search_statement_type:
        query = Q(article=search_statement_type)

    if search_statement_owner:
        query = Q(ownerAppartemnt=search_statement_owner)

    if search_statement_personal:
        query = Q(personal_book__uid__icontains=search_statement_personal)

    if search_statement_check:
        if search_statement_check == 'Не проведений':
            query &= Q(status_perfom=False)
        else:
            query &= Q(status_perfom=True)

    statements = statements.filter(query)

    start = int(request.GET.get('start', 0))
    length = int(request.GET.get('length', 10))

    paginator = Paginator(statements, length)
    statements = paginator.get_page(start // length + 1)

    data = []

    for statement in statements:
        data.append({
            'id': statement.id,
            'num': statement.uid,
            'date': statement.date_published,
            'status': statement.status_perfom,
            'type': statement.article.name_article,
            'owner': statement.ownerAppartemnt.get_full_name() if statement.ownerAppartemnt else '(не вказано)',
            'personal': statement.personal_book.uid if statement.personal_book else '(не вказано)',
            'check': statement.get_type_display(),
            'amount': statement.amount
        })

    response = {
        'draw': request.GET.get('draw'),
        'recordsTotal': Statement.objects.all().count(),
        'recordsFiltered': statements.paginator.count,
        'data': data
    }

    return JsonResponse(response)



