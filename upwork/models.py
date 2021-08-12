from django.db import models
from datetime import date

# Create your models here.

class Student(models.Model):
    firstname= models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField( max_length=100)
    age= models.CharField(max_length=10)
    dateofbirth=models.DateField(default=date.today)
    mobileno=models.CharField(max_length=10)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstname

    