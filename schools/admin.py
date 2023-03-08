from django.contrib import admin

from .models import School
from .models import Student

admin.site.register(School)
admin.site.register(Student)