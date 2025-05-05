from django.shortcuts import render
from .forms import BillForm
from .utils import calculate_bill

def bill_view(request):
    context = {}
    form = BillForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        reading = form.cleaned_data['reading']
        has_sewer = form.cleaned_data['has_sewer'] == 'yes'
        months = form.cleaned_data['months']

        result = calculate_bill(reading, has_sewer, months)
        context.update(result)

    context['form'] = form
    return render(request, 'water_bill.html', context)
