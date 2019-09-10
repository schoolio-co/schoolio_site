from django.test import TestCase
from schoolio.models import *
from schoolio.standard_matching import match_standard, match_activity

class SchoolTest(TestCase):
    def setUp(self):
        school.objects.create(name="anderson", address = "anderson")

    def test_thing(self):
        """"""
        anderson = school.objects.get(name="anderson")
        self.assertEqual(anderson.name, 'anderson')

class MatchTest(TestCase):
    def setUp(self):
        pass
