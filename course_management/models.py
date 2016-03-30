from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.name


class Lecture(models.Model):
    name = models.CharField(max_length=50)
    week = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.name
# Create your models here.
