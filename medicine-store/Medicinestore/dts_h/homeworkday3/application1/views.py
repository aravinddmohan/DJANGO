from django.shortcuts import render

# Create your views here.
def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    return render(request, 'contact.html')