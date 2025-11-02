from rest_framework import serializers
from .models import Student,Teacher,City

class StudentSerializer(serializers.ModelSerializer):
    address=serializers.StringRelatedField()
    class_teacher=serializers.StringRelatedField()

    class Meta:
        model= Student
        fields= ['id',"full_name","address","class_teacher"]


class TeacherSerializer(serializers.ModelSerializer):
    students=StudentSerializer(many=True,read_only=True)
    address=serializers.StringRelatedField()
    class Meta:
        model= Teacher
        fields= ['id',"full_name","address",'students']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model= City
        fields= ['id',"city"]
