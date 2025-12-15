from django.shortcuts import render
from .models import Customer
from .forms import CustomerForm
# Create your views here.

def add_customers(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "appcont/add_customers.html", {
                "form": CustomerForm(),
                "msg": "Customer added successfully!"
            })
    else:
        form = CustomerForm()
    return render(request, "appcont/add_customers.html", {"form": form})

def all_customers(request):
    customers = Customer.objects.all().order_by('name') 
    return render(request, 'appcont/all_customers.html', {'customers': customers})

def filtered_customers(request):
    customers = Customer.objects.filter(email__endswith='@example.com')
    return render(request, 'appcont/filtered_customers.html', {'customers': customers})