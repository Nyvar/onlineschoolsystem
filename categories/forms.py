# forms.py
from django import forms
from .models import Category, Course, Lesson, Assignment, Enrollment, Tag,Submission

class CategoryAddForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]  
class CategoryUpdateForm(forms.ModelForm):
    class Meta:
        model=Category
        fields = ["name"]
        
        
class CourseAddForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["title", "description", "price", "image", "published", "instructor", "category", "tags"]
class CourseUpdateForm(forms.ModelForm):
    class Meta:
        model=Course
        fields = ["title", "description", "price", "image", "published", "instructor", "category", "tags"]
        

class LessonAddForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ["title", "course", "video", 'video_url', "pdf", "description"]
class LessonUpdateForm(forms.ModelForm):
    class Meta:
        model=Lesson
        fields = ["title", "course", "video", 'video_url', "pdf", "description"]


class AssignmentAddForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ["course", "title", "due_date", "pdf"]



class AssignmentUpdateForm(forms.ModelForm):
    class Meta:
        model=Assignment
        fields = ["course", "title", "due_date", "pdf"]



class EnrollmentAddForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ["student", "course"]
class EnrollmentUpdateForm(forms.ModelForm):
    class Meta:
        model=Enrollment
        fields = ["student", "course"]
        
        
class TagAddForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
class TagUpdateForm(forms.ModelForm):
    class Meta:
        model=Tag
        fields = ["name"]
        
class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['file']

        
class GradeSubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['grade']
        widgets = {
            'grade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 10/12'}),
        }
        
