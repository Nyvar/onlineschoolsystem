from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages


def login_view(request):
    request.session.flush()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect based on role
            if user.role == 'student':
                return redirect('student_dashboard')
            elif user.role == 'instructor':
                return redirect('instructor_dashboard')
            elif user.role == 'employee':
                return redirect('employee_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'users/login.html')

def logout_view(request):
    request.session.flush()
    return redirect('/')