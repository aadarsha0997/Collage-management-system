from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

from .models import Student,Teacher,City
from .serializers import StudentSerializer,TeacherSerializer,CitySerializer

@api_view(["GET"])
def TeacherDashboard(request,id):
    teacher = Teacher.objects.prefetch_related('students').get(id=id) # this work same as teacher.objects.get(id=teacher id ) but difference is the performance. without this there will be 2 quairy but with this only one quiry . while fetching teacher also fetch students in one go.
    serializer=TeacherSerializer(teacher)
    content={
        'teacher': serializer.data
    }
    return Response(content)
        
@api_view(["GET"])
def StudentDashboard(req,id):
    student=Student.objects.get(id=id)
    serializer=StudentSerializer(student)
    content={
        "student": serializer.data
    }
    return Response(content)
