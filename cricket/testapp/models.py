from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User,AbstractUser
# Create your models here.
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    def __str__(self):
        return self.username

class subjects(models.Model):
    name=models.CharField(max_length=256)
    def __str__(self):
        return self.name


class teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    teacher_name = models.CharField(max_length=256,default=None)
    sub = models.ManyToManyField(subjects,related_name='students')
    def __str__(self):
        return self.user.username



class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,related_name='stds')
    student_name=models.CharField(max_length=256,default=None,null=True)
    email=models.EmailField(default=None)
    te = models.ManyToManyField(teacher,related_name='teachers')
    def __str__(self):
        return self.user.username





