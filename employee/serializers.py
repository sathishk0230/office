from rest_framework import serializers
from . import models


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = '__all__'


class OfficeSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Office
        fields = '__all__'


class VisitorSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Visitor
        fields = '__all__'
