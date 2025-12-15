from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Medicine

# signup
def signup(request):
    if request.user.is_authenticated:
         return redirect("medicine_list")
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully. Please login.")
            return redirect("login")
    else:
        form=UserCreationForm()
    return render(request,"medicinecore/signup.html",{"form":form})
# login
def login_view(request):
    if request.user.is_authenticated:
        return redirect("medicine_list")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            messages.error(request, "Both fields are required")
            return render(request, "medicinecore/login.html")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("medicine_list")
        else:
            messages.error(request, "Invalid username or password")
            return render(request, "medicinecore/login.html")

    # GET request
    return render(request, "medicinecore/login.html")



# medicinelist
@login_required
def medicine_list(request):
    query = request.GET.get("q","")

    medicines = Medicine.objects.filter(
        owner = request.user,
        name__istartswith = query
    ).order_by("-added_time")

    paginator = Paginator(medicines, 5)
    page_number = request.GET.get("page")   
    page_obj = paginator.get_page(page_number)

    return render(request, "medicinecore/medicine_list.html", {
    "page_obj": page_obj,
    "query": query
})

#addmedicine
@login_required
def add_medicine(request):
    if Medicine.objects.filter(owner=request.user).count() >= 5:
        messages.error(request,"you can only add up to 5 medicines")
        return redirect("medicine_list")
    if request.method == "POST":
        name = request.POST.get("name")
        stock = request.POST.get("stock")

        Medicine.objects.create(
            name=name,
            stock=stock,
            owner=request.user
        )
        return redirect("medicine_list")
    return render(request,"medicinecore/add_medicine.html")
# editmedicine
@login_required
def edit_medicine(request,pk):
    medicine=get_object_or_404(Medicine,id=pk,owner=request.user)
    
    if request.method == "POST":
        medicine.name = request.POST.get("name")
        medicine.stock = request.POST.get("stock")
        medicine.save()
        return redirect("medicine_list")
    return render(request, "medicinecore/edit_medicine.html", {
    "medicine": medicine
})

# deletemedicine
@login_required
def delete_medicine(request, pk):
    medicine = get_object_or_404(Medicine, id=pk, owner=request.user)
    medicine.delete()
    return redirect("medicine_list")

# logout
def logout_view(request):
    logout(request)
    return redirect("login")
