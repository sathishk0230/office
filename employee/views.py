from django.shortcuts import render
from .models import Employee
# Create your views here.


def employees(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'employee/employees.html', context=context)
