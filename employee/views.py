from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from . import models, serializers
from .forms import VisitorForm, EmployeeForm
from rest_framework import viewsets, permissions


def employees(request):
    if request.user.is_authenticated:
        employees = models.Employee.objects.all()
        context = {
            'employees': employees
        }
        return render(request, 'employee/employees.html', context=context)
    return redirect('/')


def visitors(request):
    if request.user.is_authenticated:
        visitors = models.Visitor.objects.all()
        context = {
            'visitors': visitors
        }
        return render(request, 'employee/visitor.html', context=context)
    return redirect('/')


def addv(request):
    if request.method == "POST":
        visitor = models.Visitor()
        visitor.name = request.POST.get('name', visitor.name)
        visitor.email = request.POST.get('email', visitor.email)
        visitor.visitee = models.Employee(
            request.POST.get('visitee', visitor.visitee))
        visitor.status = request.POST.get('status', visitor.status)
        visitor.save()
        return redirect('visitors')
    form = VisitorForm()
    context = {
        'form': form,
    }
    return render(request, 'employee/add_visitor.html', context=context)


def adde(request):
    if request.method == "POST":
        employee = models.Employee()
        employee.name = request.POST.get('name', employee.name)
        employee.email = request.POST.get('email', employee.email)
        employee.department = request.POST.get(
            'department', employee.department)
        employee.office = models.Office(
            request.POST.get('office', employee.office))
        employee.save()
        return redirect('employees')
    form = EmployeeForm()
    context = {
        'form': form,
    }
    return render(request, 'employee/add_visitor.html', context=context)


def updatev(request, id):
    visitor = models.Visitor.objects.get(id=id)
    form = VisitorForm(initial={
        'name': visitor.name,
        'email': visitor.email,
        'visitee': visitor.visitee,
        'status': visitor.status,
    })
    if request.method == "POST":
        visitor.name = request.POST.get('name', visitor.name)
        visitor.email = request.POST.get('email', visitor.email)
        visitor.visitee = models.Employee(
            request.POST.get('visitee', visitor.visitee))
        visitor.status = request.POST.get('status', visitor.status)
        visitor.save()
        return redirect('visitors')
    context = {
        'form': form,
        'id': id
    }
    return render(request, 'employee/update_visitor.html', context=context)


def index(request):
    return render(request, 'employee/base.html')


class EmployeeView(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializers
    permission_classes = (permissions.IsAuthenticated,)


class OfficeView(viewsets.ModelViewSet):
    queryset = models.Office.objects.all()
    serializer_class = serializers.OfficeSerializers
    permission_classes = (permissions.IsAuthenticated,)


class VisitorView(viewsets.ModelViewSet):
    queryset = models.Visitor.objects.all()
    serializer_class = serializers.VisitorSerializers
    permission_classes = (permissions.IsAuthenticated,)


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    context = {
        "form": form
    }
    return render(request, 'employee/register.html', context)
