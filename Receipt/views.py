from django.shortcuts import render
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView
from django.db.models import Q
from .models import Receipt
from .forms import ReceiptForm
# Create your views here.

class ReceiptList(ListView):
    model = Receipt
    template_name = 'Receipt/receipt_list.html'
    queryset = Receipt.objects.all()




def receipt_list(request):
    receipts = Receipt.objects.all()


    #SEARCH
    search_num_receipt = request.GET.get('num_receipt')
    search_status_receipt = request.GET.get('status_receipt')
    search_date_receipt_start = request.GET.get('date_receipt_start')
    search_date_receipt_end = request.GET.get('date_receipt_end')
    search_month_receipt = request.GET.get('month_receipt')
    search_flat_receipt = request.GET.get('flat_receipt')
    search_owner_receipt = request.GET.get('owner_receipt')
    search_check_receipt = request.GET.get('check_receipt')

    query = Q()

    if search_num_receipt:
        query &= Q(uid__icontains=search_num_receipt)

    if search_status_receipt:
        query &= Q(status_pay=search_status_receipt)

    if search_date_receipt_start:
        query &= Q(date_created__gte=search_date_receipt_start)

    if search_date_receipt_end:
        query &= Q(date_created__lte=search_date_receipt_end)

    if search_month_receipt:
        query &= Q(date_created__month=search_month_receipt)

    if search_flat_receipt:
        query &= Q(appartament__number_appartament__icontains=search_flat_receipt)

    if search_owner_receipt:
        query &= Q(appartament__owner_id=search_owner_receipt)

    if search_check_receipt:
        query &= Q(confirm=search_check_receipt)

    receipts = receipts.filter(query)




