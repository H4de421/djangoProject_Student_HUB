from django.db import models


class School(models.Model):
    """
    class School

    each school instances contain some important in formation as:
    -name
    -loction
    -the number of students
    (and an id automaticaly generated)
    """
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    nb_students = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Student(models.Model):
    """
    class student
    each student has a school
    """

    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    year = models.fields.IntegerField(default=1)
    already_graduated = models.BooleanField(default=False)

    def __str__(self):
        return self.name
