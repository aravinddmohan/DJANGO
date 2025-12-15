from django.shortcuts import render
from .forms import VisitorForm

def home(request):
    form = VisitorForm() # new form object
    return render(request, 'visitorform/home.html', {'form': form})

def result(request):
    form = VisitorForm(request.GET)  # using GET
    if form.is_valid():
        name = form.cleaned_data['name']
    else:
        name = "Guest"

    context = {
        'form': form,
        'name': name,
        'form_data': request.GET.dict()  # raw form data
    }
    return render(request, 'visitorform/result.html', context)
