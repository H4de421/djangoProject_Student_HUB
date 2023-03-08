from django.urls import reverse
from django.test import TestCase

from .models import School, Student


class Testglobal_students(TestCase):

    def test_school_number(self):
        response = self.client.get(reverse('add_stud'))
        print(response)
        self.assertQuerysetEqual(response.context['add_stud'], map(repr, []))
