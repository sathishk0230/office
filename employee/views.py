from django.shortcuts import render
from . import models, serializers
from .forms import VisitorForm
from rest_framework import viewsets, permissions


def employees(request):
    employees = models.Employee.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'employee/employees.html', context=context)


def visitors(request):
    visitors = models.Visitor.objects.all()
    context = {
        'visitors': visitors
    }
    return render(request, 'employee/visitor.html', context=context)


def addv(request):
    form = VisitorForm()
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
