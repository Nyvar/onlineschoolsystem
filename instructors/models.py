from django.db import models
from django.conf import settings

class Instructor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    username= models.CharField(max_length=100)
    password= models.CharField(max_length=128)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"Instructor: {self.user.username}"