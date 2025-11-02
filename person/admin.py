from django.contrib import admin

# Register your models here.
from . models import City,Teacher,Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('full_name','class_teacher','address')
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display=("full_name","address")
@admin.register(City)
class Admin(admin.ModelAdmin):
    list_display=('city',)