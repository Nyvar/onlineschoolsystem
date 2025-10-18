from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentAddForm, StudentUpdateForm
from users.decorators import role_required
from categories.models import Enrollment, Lesson, Assignment, Submission
from categories.forms import SubmissionForm
from django.contrib.auth import get_user_model
from django.db.models import Sum, Avg



@role_required('employee','instructor')
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})


User = get_user_model()
@role_required('instructor','employee')
def student_create(request):
    if request.method == 'POST':
        form = StudentAddForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'Username already exists.')
            else:
                user = User.objects.create_user(username=username, password=password, role='student')
                student = form.save(commit=False)
                student.user = user
                student.save()

                if hasattr(request.user, 'instructor'):
                    return redirect('instructor_dashboard')  # URL name for instructor dashboard
                elif hasattr(request.user, 'employee'):
                    return redirect('employee_dashboard')  
    else:
        form = StudentAddForm()

    return render(request, 'students/student_add.html', {'form': form})

@role_required('instructor','employee')
def student_edit(request, pk):
    student = Student.objects.filter(pk=pk).first()
    form = StudentUpdateForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        if hasattr(request.user, 'instructor'):
            return redirect('instructor_dashboard')  # URL name for instructor dashboard
        elif hasattr(request.user, 'employee'):
            return redirect('employee_dashboard') 
    return render(request, 'students/student_edit.html', {'form': form})

@role_required('instructor','employee')
def student_delete(request, pk):
    student = Student.objects.filter(pk=pk).first()
    if request.method == 'POST':
        student.user.delete()
        if hasattr(request.user, 'instructor'):
            return redirect('instructor_dashboard')  # URL name for instructor dashboard
        elif hasattr(request.user, 'employee'):
            return redirect('employee_dashboard')
    return render(request, 'students/student_delete.html', {'student': student})

def get_letter_grade(score):
    if score > 10:
        return 'A'
    elif 7 < score <= 10:
        return 'B'
    elif 5 < score <= 7:
        return 'C'
    elif 3 < score <= 5:
        return 'D'
    elif 1 < score <= 3:
        return 'E'
    elif score <= 1:
        return 'F'


@role_required('student')
def student_dashboard(request):
    student = Student.objects.get(user=request.user)
    enrollments = Enrollment.objects.filter(student=student)
    courses = [e.course for e in enrollments]
    assignments = Assignment.objects.filter(course__in=courses)
    lessons = Lesson.objects.filter(course__in=[e.course for e in enrollments])
    submission = Submission.objects.filter(student=student)
    submitted_ids = Submission.objects.filter(student=student).values_list('assignment_id', flat=True)
    upcoming_assignments = Assignment.objects.exclude(id__in=submitted_ids).filter(course__in=courses)
        
    
    scoreFromsubmissions = submission.filter(grade__isnull=False)
    total_score = scoreFromsubmissions.aggregate(total=Sum('grade'))['total'] or 0
    submission_count = scoreFromsubmissions.count()
    if submission_count>0:
        average_score = round(total_score / submission_count, 2)    
    else:
        average_score=0
        
    student.grade = get_letter_grade(average_score)
    student.save()
    if assignments.count() >0:
        progress_percent = round((submission_count / assignments.count()) * 100, 2) 
    else: 
        progress_percent=0
    context = {
        'student': student,
        'enrollments': enrollments,
        'lessons': lessons,
        'assignments': assignments,
        'submission':submission,
        'upcoming_assignments':upcoming_assignments,
        'letter_grade': student.grade,
        'progress_percent': progress_percent,
    }
    return render(request, 'students/student_dashboard.html', context)

@role_required('student')
def student_profile(request):
    student = Student.objects.get(user=request.user)
    return render(request, 'students/student_profile.html',{'student': student})
