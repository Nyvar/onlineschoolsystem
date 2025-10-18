from django.urls import path
from . import views

urlpatterns = [
    # Categories
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('categories/delete/<int:pk>/', views.category_delete, name='category_delete'),
    path('categories/add/', views.category_create, name='category_add'),

    # Courses
    path('courses/', views.course_list, name='course_list'),
    path('courses/<int:pk>/edit/', views.course_edit, name='course_edit'),
    path('courses/delete/<int:pk>/', views.course_delete, name='course_delete'),
    path('courses/add/', views.course_create, name='course_add'),
    
    path('courses/<int:pk>/lessons/', views.course_lessons, name='course_lessons'),
    path('courses/view/', views.course_view_for_student, name='course_view_for_student'),

    # Lessons
    path('lessons/', views.lesson_list, name='lesson_list'),
    path('lessons/<int:pk>/edit/', views.lesson_edit, name='lesson_edit'),
    path('lessons/delete/<int:pk>/', views.lesson_delete, name='lesson_delete'),
    path('lessons/add/', views.lesson_create, name='lesson_add'),
    
    # Assignments
    path('assignments/', views.assignment_list, name='assignment_list'),
    path('assignments/<int:pk>/edit/', views.assignment_edit, name='assignment_edit'),
    path('assignments/delete/<int:pk>/', views.assignment_delete, name='assignment_delete'),
    path('assignments/add/', views.assignment_create, name='assignment_add'),
    
    # Enrollments
    path('enrollments/', views.enrollment_list, name='enrollment_list'),
    path('enrollments/<int:pk>/edit/', views.enrollment_edit, name='enrollment_edit'),
    path('enrollments/delete/<int:pk>/', views.enrollment_delete, name='enrollment_delete'),
    path('enrollments/add/', views.enrollment_create, name='enrollment_add'),
    
    
    
    path('tags/', views.tag_list, name='tag_list'),
    path('tags/<int:pk>/edit/', views.tag_edit, name='tag_edit'),
    path('tags/delete/<int:pk>/', views.tag_delete, name='tag_delete'),
    path('tags/add/', views.tag_create, name='tag_add'),
    
    
    path('submit/<int:pk>/', views.submit_assignment, name='submit_assignment'),
    path('check/<int:pk>/', views.checking, name='checking'),
    
]
