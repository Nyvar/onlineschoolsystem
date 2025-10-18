# forms.py
from django import forms
from .models import Employee

class EmployeeAddForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ['user']
        widgets = { 
            'password': forms.PasswordInput(),
        }
class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model=Employee
        exclude = ['user']
    def save(self, commit=True):
        employee = super().save(commit=False)
        if commit:
            employee.save()
            if employee.user:
                employee.user.username = employee.username  # or any field you're syncing
                employee.user.set_password(employee.password)
                employee.user.salary= employee.salary
                employee.user.save()
        return employee
