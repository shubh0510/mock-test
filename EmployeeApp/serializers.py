from rest_framework import serializers
from EmployeeApp.models import Department,Employees

class DepartmentSerializer(serializers.modelserializer):
    class Meta:
        model=Departments
        fields=('DepartmentId', 'DepartmentName')

class EmployeeSerializer(serializers.modelserializer):
    class Meta:
        model=Employees
        fields=('EmployeeId', 'EmployeeName', 'Department', 'Dateofjoining', 'PhotoFileName')