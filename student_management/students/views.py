from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def student_detail(request, student_id):
    student = Student.objects.filter(id=student_id).first()
    if not student:
        return redirect('student_list') 
    return render(request, 'students/student_detail.html', {'student': student})

def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})

def student_update(request, student_id):
    student = Student.objects.filter(id=student_id).first()
    if not student:
        return redirect('student_list')
    
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form})

def student_confirm_delete(request, pk):
    student = Student.objects.get(id=pk)
    return render(request, 'students/student_confirm.html', {'student': student})

def student_delete(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return redirect('student_list') 