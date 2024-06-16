from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question=models.CharField(max_length=100)
    answer=models.IntegerField()
    options_one=models.CharField(max_length=100)
    options_two=models.CharField(max_length=100)
    options_three=models.CharField(max_length=100,blank=True)
    options_four=models.CharField(max_length=100,blank=True)
    marks=models.IntegerField(default=5)
    def __str__(self):
        return self.question

class ScoreBoard(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    score=models.IntegerField(default=0)