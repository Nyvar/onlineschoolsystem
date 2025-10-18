from django.shortcuts import render, redirect
from .models import Category, Course, Lesson, Assignment, Enrollment, Tag, Submission
from .forms import CategoryAddForm, CategoryUpdateForm, CourseAddForm, CourseUpdateForm, LessonAddForm, LessonUpdateForm, AssignmentAddForm, AssignmentUpdateForm, EnrollmentAddForm, EnrollmentUpdateForm ,TagAddForm, TagUpdateForm ,SubmissionForm,GradeSubmissionForm
from users.decorators import role_required
# from categories.models import Enrollment, Lesson, Assignment

@role_required('instructor','employee')
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/category_list.html', {'categories': categories})

@role_required('instructor','employee')
def category_create(request):
    if request.method == 'POST':
        form = CategoryAddForm(request.POST)
        if form.is_valid():
            form.save()
            if hasattr(request.user, 'instructor'):
                return redirect('instructor_dashboard')  # URL name for instructor dashboard
            elif hasattr(request.user, 'employee'):
                return redirect('employee_dashboard') 
    else:
        form = CategoryAddForm()
    return render(request, 'categories/category_add.html', {'form': form})

@role_required('instructor','employee')
def category_edit(request, pk):
    category = Category.objects.filter( pk=pk).first()
    form = CategoryUpdateForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        if hasattr(request.user, 'instructor'):
            return redirect('instructor_dashboard')  # URL name for instructor dashboard
        elif hasattr(request.user, 'employee'):
            return redirect('employee_dashboard') 
    return render(request, 'categories/category_edit.html', {'form': form, 'category': category})

@role_required('instructor','employee')
def category_delete(request, pk):
    category = Category.objects.filter(pk=pk).first()
    if request.method == 'POST':
        category.delete()
        if hasattr(request.user, 'instructor'):
            return redirect('instructor_dashboard')  # URL name for instructor dashboard
        elif hasattr(request.user, 'employee'):
            return redirect('employee_dashboard') 
    return render(request, 'categories/category_delete.html', {'category': category})




@role_required('instructor','employee')
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})
@role_required('instructor','employee')
def course_create(request):
    if request.method == 'POST':
        form = CourseAddForm(request.POST , request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.save()
            if hasattr(request.user, 'instructor'):
                return redirect('instructor_dashboard')  # URL name for instructor dashboard
            elif hasattr(request.user, 'employee'):
                return redirect('employee_dashboard')   
    else:
        form = CourseAddForm()
    return render(request, 'courses/course_add.html', {'form': form})
@role_required('instructor','employee')
def course_edit(request, pk):
    course = Course.objects.filter(pk=pk).first()
    form = CourseUpdateForm(request.POST, request.FILES, instance=course)
    if form.is_valid():
        form.save()
        if hasattr(request.user, 'instructor'):
            return redirect('instructor_dashboard')  # URL name for instructor dashboard
        elif hasattr(request.user, 'employee'):
            return redirect('employee_dashboard')  
    return render(request, 'courses/course_edit.html', {'form': form})
@role_required('instructor','employee')
def course_delete(request, pk):
    course = Course.objects.filter(pk=pk).first()
    if request.method == 'POST':
        course.delete()
        if hasattr(request.user, 'instructor'):
            return redirect('instructor_dashboard')  # URL name for instructor dashboard
        elif hasattr(request.user, 'employee'):
            return redirect('employee_dashboard') 
    return render(request, 'courses/course_delete.html', {'course': course})





@role_required('instructor','employee')
def lesson_list(request):
    lessons = Lesson.objects.all()
    return render(request, 'lessons/lesson_list.html', {'lessons': lessons})
@role_required('instructor','employee')
def lesson_create(request):
    if request.method == 'POST':
        form = LessonAddForm(request.POST, request.FILES)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.save()
            if hasattr(request.user, 'instructor'):
                return redirect('instructor_dashboard')  # URL name for instructor dashboard
            elif hasattr(request.user, 'employee'):
                return redirect('employee_dashboard')   
    else:
        form = LessonAddForm()
    return render(request, 'lessons/lesson_add.html', {'form': form})
@role_required('instructor','employee')
def lesson_edit(request, pk):
    lesson = Lesson.objects.filter(pk=pk).first()
    form = LessonUpdateForm(request.POST or None, instance=lesson)
    if form.is_valid():
        form.save()
        if hasattr(request.user, 'instructor'):
            return redirect('instructor_dashboard')  # URL name for instructor dashboard
        elif hasattr(request.user, 'employee'):
            return redirect('employee_dashboard')  
    return render(request, 'lessons/lesson_edit.html', {'form': form})
@role_required('instructor','employee')
def lesson_delete(request, pk):
    lesson = Lesson.objects.filter(pk=pk).first()
    if request.method == 'POST':
        lesson.delete()
        if hasattr(request.user, 'instructor'):
            return redirect('instructor_dashboard')  # URL name for instructor dashboard
        elif hasattr(request.user, 'employee'):
            return redirect('employee_dashboard') 
    return render(request, 'lessons/lesson_delete.html', {'lesson': lesson})





@role_required('instructor','employee')
def assignment_list(request):
    assignments = Assignment.objects.all()
    return render(request, 'assignments/assignment_list.html', {'assignments': assignments})
@role_required('instructor','employee')
def assignment_create(request):
    if request.method == 'POST':
        form = AssignmentAddForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.save()
            if hasattr(request.user, 'instructor'):
                return redirect('instructor_dashboard')  # URL name for instructor dashboard
            elif hasattr(request.user, 'employee'):
                return redirect('employee_dashboard') 
    else:
        form = AssignmentAddForm()
    return render(request, 'assignments/assignment_add.html', {'form': form})

@role_required('instructor','employee')
def assignment_edit(request, pk):
    assignment = Assignment.objects.filter(pk=pk).first()
    form = AssignmentUpdateForm(request.POST or None, instance=assignment)
    if form.is_valid():
        form.save()
        if hasattr(request.user, 'instructor'):
            return redirect('instructor_dashboard')  # URL name for instructor dashboard
        elif hasattr(request.user, 'employee'):
            return redirect('employee_dashboard')  
    return render(request, 'assignments/assignment_edit.html', {'form': form})
@role_required('instructor','employee')
def assignment_delete(request, pk):
    assignment = Assignment.objects.filter(pk=pk).first()
    if request.method == 'POST':
        assignment.delete()
        if hasattr(request.user, 'instructor'):
            return redirect('instructor_dashboard')  # URL name for instructor dashboard
        elif hasattr(request.user, 'employee'):
            return redirect('employee_dashboard') 
    return render(request, 'assignments/assignment_delete.html', {'assignment': assignment})




@role_required('instructor','employee')
def enrollment_list(request):
    enrollments = Enrollment.objects.all()
    return render(request, 'enrollments/enrollment_list.html', {'enrollments': enrollments})
@role_required('instructor','employee')
def enrollment_create(request):
    if request.method == 'POST':
        form = EnrollmentAddForm(request.POST)
        if form.is_valid():
            enrollment = form.save(commit=False)
            enrollment.save()
            if hasattr(request.user, 'instructor'):
                return redirect('instructor_dashboard')  # URL name for instructor dashboard
            elif hasattr(request.user, 'employee'):
                return redirect('employee_dashboard')   
    else:
        form = EnrollmentAddForm()
    return render(request, 'enrollments/enrollment_add.html', {'form': form})
@role_required('instructor','employee')
def enrollment_edit(request, pk):
    enrollment = Enrollment.objects.filter(pk=pk).first()
    form = EnrollmentUpdateForm(request.POST or None, instance=enrollment)
    if form.is_valid():
        form.save()
        if hasattr(request.user, 'instructor'):
            return redirect('instructor_dashboard')  # URL name for instructor dashboard
        elif hasattr(request.user, 'employee'):
            return redirect('employee_dashboard')  
    return render(request, 'enrollments/enrollment_edit.html', {'form': form})
@role_required('instructor','employee')
def enrollment_delete(request, pk):
    enrollment = Enrollment.objects.filter(pk=pk).first()
    if request.method == 'POST':
        enrollment.delete()
        if hasattr(request.user, 'instructor'):
            return redirect('instructor_dashboard')  # URL name for instructor dashboard
        elif hasattr(request.user, 'employee'):
            return redirect('employee_dashboard') 
    return render(request, 'enrollments/enrollment_delete.html', {'enrollment': enrollment})




@role_required('instructor','employee','student')
def course_lessons(request, pk):
    course = Course.objects.filter(pk=pk).first()
    lessons = Lesson.objects.filter(course=course )

    context = {
        'course': course,
        'lessons': lessons,
    }
    return render(request, 'courses/course_lessons.html', context)

@role_required('instructor','employee','student')
def course_view_for_student(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_view_for_student.html', {'courses': courses})


@role_required('instructor','employee')
def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'tags/tag_list.html', {'tags': tags})
@role_required('instructor','employee')
def tag_create(request):
    if request.method == 'POST':
        form = TagAddForm(request.POST)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.save()
            if request.user.is_authenticated and hasattr(request.user, 'instructor'):
                return redirect('instructor_dashboard')
            elif request.user.is_authenticated and hasattr(request.user, 'employee'):
                return redirect('employee_dashboard')  
    else:
        form = TagAddForm()
    return render(request, 'tags/tag_add.html', {'form': form})
@role_required('instructor','employee')
def tag_edit(request, pk):
    tag =Tag.objects.filter(pk=pk).first()
    form = TagUpdateForm(request.POST or None, instance=tag)
    if form.is_valid():
        form.save()
        if hasattr(request.user, 'instructor'):
            return redirect('instructor_dashboard')  # URL name for instructor dashboard
        elif hasattr(request.user, 'employee'):
            return redirect('employee_dashboard')  
    return render(request, 'tags/tag_edit.html', {'form': form})
@role_required('instructor','employee')
def tag_delete(request, pk):
    tag = Tag.objects.filter(pk=pk).first()
    if request.method == 'POST':
        tag.delete()
        if hasattr(request.user, 'instructor'):
            return redirect('instructor_dashboard')  # URL name for instructor dashboard
        elif hasattr(request.user, 'employee'):
            return redirect('employee_dashboard') 
    return render(request, 'tags/tag_delete.html', {'tag': tag})



def submit_assignment(request, pk):
    assignment = Assignment.objects.get(pk=pk)
    student = request.user.student

    if request.method == 'POST':
        # submit=Submission.objects.filter(pk=pk).first()
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.assignment = assignment
            submission.student = student
            submission.save()
            return redirect('student_dashboard')
    else:
        form = SubmissionForm()

    return render(request, 'submision/sumit.html', {'form': form})


def checking(request, pk):
    submission =Submission.objects.get(pk=pk)

    if request.method == 'POST':
        form = GradeSubmissionForm(request.POST, instance=submission)
        if form.is_valid():
            form.save()
            return redirect('instructor_dashboard')  
    else:
        form = GradeSubmissionForm(instance=submission)

    return render(request, 'submision/grading.html', {'form': form})