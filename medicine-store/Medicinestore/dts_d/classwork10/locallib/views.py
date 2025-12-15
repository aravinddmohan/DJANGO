from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from .models import Book
from .forms import BookForm
from django.shortcuts import get_object_or_404
# Create your views here.

def home(request):
    books_list = Book.objects.all().order_by('id')
    paginator=Paginator(books_list,5)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    return render(request,'locallib/home.html',{'page_obj':page_obj})

def add_book(request):
    form=None
    if request.method=='POST':
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form=BookForm()
        
    return render(request,'locallib/add_book.html',{'form':form})
        
def edit_book(request,pk):
    book = get_object_or_404(Book, id=pk)
    book=Book.objects.get(id=pk)
    if request.method=='POST':
        form=BookForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=BookForm(instance=book)

    return render(request,'locallib/edit_book.html',{'form':form})

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.delete()
        return redirect('home')

    return render(request, 'locallib/delete_book.html', {'book': book})