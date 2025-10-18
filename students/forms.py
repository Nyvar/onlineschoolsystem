# forms.py
from django import forms
from .models import Student

class StudentAddForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['user','grade']
        widgets = { #just custome the password field to be style hidden as user input 
            'password': forms.PasswordInput(),
        }
class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['user','grade']

    def save(self, commit=True):
        student = super().save(commit=False)
        if commit:
            student.save()
            if student.user:
                student.user.username = student.username
                student.user.set_password(student.password)
                student.user.save()
        return student
