from django.shortcuts import render

def home(request):
    return render(request,"multilevel/homepage.html")

def about(request):
    return render(request,"multilevel/about.html")
