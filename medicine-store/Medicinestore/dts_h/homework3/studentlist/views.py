from django.shortcuts import render

# Create your views here.
students = [
    {'name': 'Aravind',  'grade': 'A', 'passed': True,},
    {'name': 'Michael',  'grade': 'B', 'passed': True,},
    {'name': 'Charlie',  'grade': 'C', 'passed': True,},
    {'name': 'Thomas',  'grade': 'D', 'passed': False,},
    {'name': 'James',  'grade': 'F', 'passed': False,},
]

def student_list(request):
    return render(request, 'studentlist/studentlist.html', {'students': students})

