from django.db import models
class City(models.Model):
    city=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.city}"

    class Meta:
        verbose_name_plural='AddressDB'

class Teacher(models.Model):
    full_name=models.CharField(max_length=100,default="Teacher")
    address=models.ForeignKey(City,blank=True,null=True,on_delete=models.CASCADE,)

    def __str__(self):
        return f"{self.full_name}"

    class Meta:
        verbose_name_plural='TeacherDB'

# Create your models here.
class Student(models.Model):
    full_name=models.CharField( max_length=50)
    address=models.ForeignKey(City,blank=True, null=True,on_delete=models.CASCADE,)
    class_teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE,blank=True,null=True,related_name='students')
    
    class Meta:
        verbose_name_plural='StudentDB'


