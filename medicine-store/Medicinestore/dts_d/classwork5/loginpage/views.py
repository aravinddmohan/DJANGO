from django.shortcuts import render
from .forms import LoginForm

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            return render(request, 'loginpage/success.html', {'email': email,})
    else:
        form = LoginForm()
    return render(request, 'loginpage/login.html', {'form': form})