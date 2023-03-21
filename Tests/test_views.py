from django.urls import reverse
from django.test import TestCase

from .models import School, Student


class Testglobal_students(TestCase):

    def setUp(self):
        school1 = School.objects.create(name="test_01",location="nowhere",nb_students=2,id=421)
        stud1 = Student.objects.create(school_id=School.objects.get(name="test_01").id,name="stud_1",year="2",already_graduated=True)
        stud2 = Student.objects.create(school_id=School.objects.get(name="test_01").id,name="stud_2",year="2",already_graduated=True)

    def test_school_number(self):
        school1 = School.objects.create(name="test_03", location="nowhere", nb_students=2, id=423)
        stud1 = Student.objects.create(school_id=School.objects.get(name="test_03'").id, name="stud_1", year="2",
                                       already_graduated=True)
        print(type(stud1.school.id))
        print(type(school1.id))
        #stud2 = Student.objects.create(school_id=School.objects.get(name="test_01").id, name="stud_2", year="2",already_graduated=True)
        #self.assertIs(stud1.school.id, school1.id)
        #response = self.client.get(reverse('add_stud'))
        #print(response)
        return True
