from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeAddForm, EmployeeUpdateForm
from users.decorators import role_required
from categories.models import Enrollment, Lesson, Assignment, Category, Course, Tag
from students.models import Student
from instructors.models import Instructor
from django.contrib.auth import get_user_model

@role_required('employee')
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})


User = get_user_model()
@role_required('employee')
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeAddForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'Username already exists.')
            else:
                user = User.objects.create_user(username=username, password=password, role='employee')
                employee = form.save(commit=False)
                employee.user = user
                employee.save()

                return redirect('employee_dashboard')  
    else:
        form = EmployeeAddForm()

    return render(request, 'employees/employee_add.html', {'form': form})

@role_required('employee')
def employee_edit(request, pk):
    employee = Employee.objects.filter(pk=pk).first()
    form = EmployeeUpdateForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('employee_dashboard') 
    return render(request, 'employees/employee_edit.html', {'form': form})

@role_required('employee')
def employee_delete(request, pk):
    employee = Employee.objects.filter(pk=pk).first()
    if request.method == 'POST':
        employee.user.delete()
        return redirect('employee_dashboard')
    return render(request, 'employees/employee_delete.html', {'employee': employee})



@role_required('employee')
def employee_dashboard(request):
    return render(request, 'employees/employee_dashboard.html')

def employee_sum(request):
    context = {
        'total_employees': Employee.objects.count(),
        'total_students': Student.objects.count(),
        'total_instructors': Instructor.objects.count(),
        'total_courses': Course.objects.count(),
    }
    return render(request, 'employees/em_sum.html', context)



@role_required('employee')
def load_partial(request, page_name):
    if page_name == 'category_list':
        categories = Category.objects.all()
        return render(request, 'categories/category_list.html', {'categories': categories})
    elif page_name == 'course_list':
        courses = Course.objects.all()
        return render(request, 'courses/course_list.html', {'courses': courses})
    elif page_name == 'lesson_list':
        lessons = Lesson.objects.all()
        return render(request, 'lessons/lesson_list.html', {'lessons': lessons})
    elif page_name == 'assignment_list':
        assignments = Assignment.objects.all()
        return render(request, 'assignments/assignment_list.html', {'assignments': assignments})
    elif page_name == 'enrollment_list':
        enrollments = Enrollment.objects.all()
        return render(request, 'enrollments/enrollment_list.html', {'enrollments': enrollments})
    elif page_name == 'student_list':
        students = Student.objects.all()
        return render(request, 'students/student_list.html', {'students': students})
    elif page_name == 'instructor_list':
        instructors = Instructor.objects.all()
        return render(request, 'instructors/instructor_list.html', {'instructors': instructors})
    elif page_name == 'employee_list':
        employees = Employee.objects.all()
        return render(request, 'employees/employee_list.html', {'employees': employees})
    elif page_name == 'tag_list':
        tags = Tag.objects.all()
        return render(request, 'tags/tag_list.html', {'tags': tags})
    elif page_name == 'em_sum':
        context = {
            'total_employees': Employee.objects.count(),
            'total_students': Student.objects.count(),
            'total_instructors': Instructor.objects.count(),
            'total_courses': Course.objects.count(),
        }
        return render(request, 'employees/em_sum.html', context)
    return render(request, f'employees/{page_name}.html')
