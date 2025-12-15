from django.shortcuts import render

# Create your views here.
def employee_list(request):
    employees = [
        {'name': 'aravind', 'job-title': 'developer',"salary": 60000,'full_time': True},
        {'name': 'ashik', 'job-title': 'tester',"salary": 100000,'full_time': True},
        {'name': 'keerthy', 'job-title': 'analyst',"salary": 50000,'full_time': False},
        {'name': 'kevin', 'job-title': 'builder',"salary": 90000,'full_time': True},]
    context = {'employee': employees}
    return render(request, 'employeedirectory/employeelist.html', context)
