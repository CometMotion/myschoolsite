# schoolapp/views.py
from django.shortcuts import render, redirect
from .models import Student, Grade
from .forms import StudentForm

def students_list(request):
    students = Student.objects.all()
    return render(request, 'students_list.html', {'students': students})

def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    grades = Grade.objects.filter(student=student)
    return render(request, 'student_detail.html', {'student': student, 'grades': grades})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students_list')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})