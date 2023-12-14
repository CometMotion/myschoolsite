# schoolapp/urls.py
from django.urls import path
from .views import students_list, student_detail, add_student, delete_student

urlpatterns = [
    path('students/', students_list, name='students_list'),
    path('students/<int:student_id>/', student_detail, name='student_detail'),
    path('add_student/', add_student, name='add_student'),
    path('delete_student/<int:student_id>/', delete_student, name='delete_student'),
]


