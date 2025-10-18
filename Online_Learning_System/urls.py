"""
URL configuration for Online_Learning_System project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from students import urls as student_urls
from users import urls as user_urls
from users import views as user_views  # Assuming your login view is in users/views.py
from django.conf import settings
from django.conf.urls.static import static
from employees import urls as employee_urls
from instructors import urls as instructor_urls
from categories import urls as category_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/',include(student_urls) ),
    path('', user_views.login_view, name='home'),  
    path('logout/', user_views.logout_view, name='logout'), 
    path('employees/',include(employee_urls) ),
    path('instructors/',include(instructor_urls) ),
    path('',include(category_urls) ),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

