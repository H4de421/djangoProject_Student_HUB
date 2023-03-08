
from django import forms
from schools.models import Student, School

class Student_forms(forms.ModelForm):
   class Meta:
       model = Student
       fields = '__all__'

class School_forms(forms.ModelForm):
   class Meta:
       model = School
       fields = 'name','location'