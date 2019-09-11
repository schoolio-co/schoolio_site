from django.test import TestCase
from schoolio.models import *

class HomePageTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)


class SchoolTest(TestCase):
    def setUp(self):
        school.objects.create(name="anderson", address = "anderson")

    def test_thing(self):
        """"""
        anderson = school.objects.get(name="anderson")
        self.assertEqual(str(anderson), 'anderson')