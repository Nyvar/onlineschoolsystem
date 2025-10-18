from django.db import models
from instructors.models import Instructor
from students.models import Student



class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.FileField(upload_to='course_image/', null=True, blank=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    instructor=models.ForeignKey(Instructor, on_delete=models.SET_NULL,null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    def __str__(self):
        return self.title
    
class Lesson(models.Model):
    title= models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    video = models.FileField(upload_to='lessons_videos/', null=True, blank=True)
    video_url = models.URLField(blank=True, null=True)
    pdf = models.FileField(upload_to='lessons_image/', null=True, blank=True)
    description = models.TextField()
    def __str__(self):
        return self.title
    
class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    due_date = models.DateField()
    pdf=models.FileField(upload_to='assignments_image/', null=True, blank=True)
    def __str__(self):
        return f"{self.title} ({self.course.title})"  
      
class Enrollment(models.Model):
    student= models.ForeignKey(Student, on_delete=models.CASCADE)    
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self):
     return f"{self.student.user.username} enrolled in {self.course.title}"

class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    file = models.FileField(upload_to='submissions/')
    grade = models.CharField(max_length=10, blank=True)  # e.g. "12/12"