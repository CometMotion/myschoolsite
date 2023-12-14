# schoolapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
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

def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('students_list')
    return render(request, 'delete_student.html', {'student': student})