# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('<int:pk>/edit/', views.employee_edit, name='employee_edit'),
    path('delete/<int:pk>/', views.employee_delete, name='employee_delete'),
    path('add/', views.employee_create, name='employee_add'),
    path('dashboard/', views.employee_dashboard, name='employee_dashboard'),
    path('em_sum/',views.employee_sum, name='emplyoee_sum'),
    path('load/<str:page_name>/', views.load_partial, name='load_partial'),

    
]
