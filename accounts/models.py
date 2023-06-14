from django.db import models


class Student(models.Model):
    roll_number = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField(help_text='Format: YYYY-MM-DD')

    def __str__(self):
        return self.name



class MarkStudent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    mark = models.FloatField()