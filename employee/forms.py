from . import models
from django import forms


class VisitorForm(forms.ModelForm):
    class Meta:
        model = models.Visitor
        fields = '__all__'


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = models.Employee
        fields = '__all__'
