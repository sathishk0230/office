from django.shortcuts import render
from . import models, serializers
from rest_framework import viewsets, permissions


def employees(request):
    employees = models.Employee.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'employee/employees.html', context=context)


def index(request):
    return render(request, 'employee/base.html')


class EmployeeView(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class OfficeView(viewsets.ModelViewSet):
    queryset = models.Office.objects.all()
    serializer_class = serializers.OfficeSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class VisitorView(viewsets.ModelViewSet):
    queryset = models.Visitor.objects.all()
    serializer_class = serializers.VisitorSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
