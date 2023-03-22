from django.urls import reverse
from django.test import TestCase

from .models import School, Student


class Testglobal_students(TestCase):

    def test_school_number(self):
        school1 = School(name="test_01", location="nowhere", nb_students=1)
        school2 = School(name="test_02", location="nowhere", nb_students=1)
        school1.save(school1)
        school2.save(school2)
        stud1 = Student.objects.create(school_id=School.objects.get(name="test_01").id, name="stud_1", year="2",already_graduated=True)
        stud2 = Student.objects.create(school_id=School.objects.get(name="test_02").id, name="stud_2", year="2",already_graduated=True)

        self.assertTrue(stud1.school.id == school1.id,"stud1 attend the second school")
        self.assertFalse(stud2.school.id == school1.id, "stud2 attend the first school")
        return True

class index_test(TestCase):

    def test_no_school(self):
        """
            If no school exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('Schools:index'))
        print(response.context)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No schools are available.")
        self.assertQuerysetEqual(response.context['longer_school_list'], map(repr, []))
