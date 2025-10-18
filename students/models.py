from django.db import models
from django.conf import settings

class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    grade = models.CharField(max_length=10)
    username= models.CharField(max_length=100)
    password= models.CharField(max_length=128)
    def __str__(self):
        return f"student: {self.user.username}"
