from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Department,Employees
from EmployeeApp.serializers import DepartmentSerializer,EmployeeSerializer

# Create your views here.

@csrf_exempt
def departmentApi(request,id=0):
    if request.method=='GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments,many=True)
        return JsonResponse(departments_serializer.data,safe=False)
    elif request.method=='POST':
        depament_data=JSONparser().parser(request)
        departments_serializer=DepartmentSerializer(data=depament_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method=='PUT':
        depament_data=JSONparser().purse(request)
        department=Departments.objects.get(DepartmentId=depament_data['DepartmentId'])
        departments_serializer=DepartmentSerializer(department,data=depament_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method=='DELETE':
        department=Departments.objects.get(DepartmentId=Id)
        department.delete()
        return JsonResponse("Deleted Successfully", safe=False)