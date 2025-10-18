from django.shortcuts import render, redirect
from .models import Instructor
from .forms import InstructorAddForm, InstructorUpdateForm
from users.decorators import role_required
from categories.models import Enrollment, Lesson, Assignment, Category, Course,Tag
from students.models import Student
from categories.models import Submission
from django.db.models import Sum

from django.contrib.auth import get_user_model

@role_required('instructor','employee')
def instructor_list(request):
    instructors = Instructor.objects.all()
    return render(request, 'instructors/instructor_list.html', {'instructors': instructors})


User = get_user_model()
@role_required('instructor','employee')
def instructor_create(request):
    if request.method == 'POST':
        form = InstructorAddForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'Username already exists.')
            else:
                user = User.objects.create_user(username=username, password=password, role='instructor')
                instructor = form.save(commit=False)
                instructor.user = user
                instructor.save()

                return redirect('instructor_dashboard')  
    else:
        form =InstructorAddForm()

    return render(request, 'instructors/instructor_add.html', {'form': form})

@role_required('employee')
def instructor_edit(request, pk):
    instructor = Instructor.objects.filter(pk=pk).first()
    form = InstructorUpdateForm(request.POST or None, instance=instructor)
    if form.is_valid():
        form.save()
        if hasattr(request.user, 'instructor'):
            return redirect('instructor_dashboard')  # URL name for instructor dashboard
        elif hasattr(request.user, 'employee'):
            return redirect('employee_dashboard') 
    return render(request, 'instructors/instructor_edit.html', {'form': form})

@role_required('employee')
def instructor_delete(request, pk):
    instructor = Instructor.objects.filter(pk=pk).first()
    if request.method == 'POST':
        instructor.user.delete()
        if hasattr(request.user, 'instructor'):
            return redirect('instructor_dashboard')  # URL name for instructor dashboard
        elif hasattr(request.user, 'employee'):
            return redirect('employee_dashboard')
    return render(request, 'instructors/instructor_delete.html', {'instructor': instructor})

@role_required('instructor')
def instructor_sum(request):
    instructor = Instructor.objects.get(user=request.user)
    course= Course.objects.filter(instructor=instructor)
    course_count=course.count()
    
   
    student = Enrollment.objects.filter(course__in=course) 
    student_count=student.count()
    salary=instructor.salary
    
    assignments = Assignment.objects.filter(course__in=course)
    submissions = Submission.objects.filter(assignment__in=assignments)
    
    context = {
        'total_course': course_count,
        'total_students': student_count,
        'total_salary': salary,
        'underreview': submissions,
    }
    return render(request, 'instructors/instr_sum.html', context)




@role_required('instructor')
def load_partial(request, page_name):
    instructor = Instructor.objects.get(user=request.user)
    
    if page_name == 'category_list':
        categories = Category.objects.all()
        return render(request, 'categories/category_list.html', {'categories': categories})

    elif page_name == 'course_list':
        courses = Course.objects.filter(instructor=instructor)
        return render(request, 'courses/course_list.html', {'courses': courses})

    elif page_name == 'lesson_list':
        lessons = Lesson.objects.filter(course__in=Course.objects.filter(instructor=instructor))
        return render(request, 'lessons/lesson_list.html', {'lessons': lessons})

    elif page_name == 'assignment_list':
        assignments = Assignment.objects.filter(course__in=Course.objects.filter(instructor=instructor))
        return render(request, 'assignments/assignment_list.html', {'assignments': assignments})

    elif page_name == 'enrollment_list':
        enrollments = Enrollment.objects.filter(course__in=Course.objects.filter(instructor=instructor))
        return render(request, 'enrollments/enrollment_list.html', {'enrollments': enrollments})

    elif page_name == 'student_list':
        students = Student.objects.filter(enrollment__course__in=Course.objects.filter(instructor=instructor)).distinct()
        return render(request, 'students/student_list.html', {'students': students})

    elif page_name == 'tag_list':
        tags = Tag.objects.all()
        return render(request, 'tags/tag_list.html', {'tags': tags})

    elif page_name == 'instr_sum':
        courses = Course.objects.filter(instructor=instructor)
        enrollments = Enrollment.objects.filter(course__in=courses)
       
        context = {
            'total_course': courses.count(),
            'total_students': enrollments.count(),
            'total_salary': instructor.salary,
          
        }
        return render(request, 'instructors/instr_sum.html', context)

    # Default fallback
    return render(request, f'instructors/{page_name}.html')


        

@role_required('instructor')
def instructor_dashboard(request):
    return render(request, 'instructors/instructor_dashboard.html')

@role_required('instructor')
def review_submission(request):
    submissions = Submission.objects.all()
    
    return render(request, 'instructors/review_submission.html', {'submissions': submissions})
