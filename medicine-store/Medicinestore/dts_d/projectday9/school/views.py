from django.shortcuts import render

# Create your views here.
students={
    'aravind': {'science': 60, 'maths': 70, 'english': 90},
    'kumar': {'science': 80, 'maths': 90, 'english': 70},
    'raja': {'science': 70, 'maths': 60, 'english': 80},
    'vijay': {'science': 90, 'maths': 80, 'english': 60},
    'ajith': {'science': 50, 'maths': 40, 'english':50},
}
def home(request):
    return render(request, 'students/home.html', {'students': students.keys()})

def results(request,name):
    student=students.get(name.lower())
    return render(request, 'students/result.html', {'name': name, 'student': student,})