# forms.py
from django import forms
from .models import Instructor

class InstructorAddForm(forms.ModelForm):
    class Meta:
        model = Instructor
        exclude = ['user']
        widgets = { 
            'password': forms.PasswordInput(),
        }
class InstructorUpdateForm(forms.ModelForm):
    class Meta:
        model=Instructor
        exclude = ['user']
    def save(self, commit=True):
        instructor = super().save(commit=False)
        if commit:
            instructor.save()
            # Sync username with linked User model
            if instructor.user:
                instructor.user.username = instructor.username  # or any field you're syncing
                instructor.user.set_password(instructor.password)
                instructor.user.salary= instructor.salary
                instructor.user.save()
        return instructor
        
