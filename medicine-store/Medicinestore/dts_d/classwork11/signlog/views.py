from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def sign_up(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,'signlog/signup.html',{'form':form})


def log_in(request):
    if request.method=="POST":
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return(redirect('visit'))
    else:
        form=AuthenticationForm()
    return(render(request,'signlog/login.html',{'form':form}))

@login_required
def visit_counter(request):
    visits=request.session.get('visits',0)
    visits+=1
    request.session['visits']=visits
    return(render(request,'signlog/visit.html',{'visits':visits}))

@login_required
def logout_view(request):
    if request.method=="POST":
        logout(request)
        return(redirect('login'))
    
    return(render(request,'signlog/logout.html'))