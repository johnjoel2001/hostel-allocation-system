from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user=models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True,blank=True)
    registration=models.CharField(max_length=200,null=True,blank=True)
    is_nine_pointer=models.BooleanField(null=True,blank=True)
    def __str__(self):
        return self.name

class Choice(models.Model):
    choices=models.CharField(max_length=200,null=True,blank=True)
   

class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField(max_length=122)
    date=models.DateField()    

# Create your models here.
