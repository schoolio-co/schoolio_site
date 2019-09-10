from django.test import TestCase
from schoolio.models import *


class SchoolTest(TestCase):
    def setUp(self):
        school.objects.create(name="anderson", address = "anderson")

    def test_thing(self):
        """"""
        anderson = school.objects.get(name="anderson")
        self.assertEqual(str(anderson), 'anderson')

