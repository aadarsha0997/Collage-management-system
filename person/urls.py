from django.urls import path
from . import views

urlpatterns = [
    path('teacher/<int:id>/',views.TeacherDashboard)
]
