from django.shortcuts import render,redirect,get_object_or_404
from .models import Student
from .forms import StudentForm

# Create your views here.
def student_list(request):
    