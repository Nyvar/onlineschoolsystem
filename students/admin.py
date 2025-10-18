from django import forms
from django.contrib import admin
from .models import Student
from django.contrib.auth import get_user_model

User = get_user_model() # as current user
# the entire code here is abt : create a user and link it to the role Student

class StudentAddForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(StudentAddForm, self).__init__(*args, **kwargs)  
        self.fields['user'].queryset = User.objects.filter(role='student') # filter the role of user to just student

class StudentAdmin(admin.ModelAdmin):
    form = StudentAddForm

admin.site.register(Student, StudentAdmin)
