# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.instructor_list, name='instructor_list'),
    path('<int:pk>/edit/', views.instructor_edit, name='instructor_edit'),
    path('delete/<int:pk>/', views.instructor_delete, name='instructor_delete'),
    path('add/', views.instructor_create, name='instructor_add'),
    path('dashboard/', views.instructor_dashboard, name='instructor_dashboard'),
    path('instr_sum/', views.instructor_sum, name='instructor_sum'),
    path('review/', views.review_submission, name='review_submission'),
    path('load/<str:page_name>/', views.load_partial, name='load_partial'),

    
]
