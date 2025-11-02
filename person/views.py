from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

from .models import Student,Teacher,City
from .serializers import StudentSerializer,TeacherSerializer,CitySerializer

@api_view(["GET"])
def TeacherDashboard(request,id):
    teacher_id=id
    teacher = Teacher.objects.prefetch_related('students').get(id=teacher_id)
    serializer=TeacherSerializer(teacher)
    content={
        'teacher': serializer.data
    }
    return Response(content)
        
