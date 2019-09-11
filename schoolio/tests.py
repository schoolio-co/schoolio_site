from django.test import TestCase
from schoolio.models import *
from schoolio.standard_matching import match_standard, match_activity
from schoolio.evaluate import get_MI_BL

class SchoolTest(TestCase):
    def setUp(self):
        school.objects.create(name="anderson", address = "anderson")

    def test_thing(self):
        """"""
        anderson = school.objects.get(name="anderson")

        self.assertEqual(anderson.name, 'anderson')

class MatchTest(TestCase):
    def setUp(self):
        school.objects.create(name="anderson", address = "anderson")
        User.objects.create(first_name = "Carolyn", last_name = "Luc", email = "as@fid.ohv", school="anderson"
            username="cluc")
        grade_level.objects.create(grade = "1st", school = "anderson")
        classroom.objects.create(classroom="unique", grade = "1st", school="anderson", teacher = "cluc")
        classroom_subject_summary.objects.create(classroom="unique", subject="Mathematics", lu_level = 45, mu_level = 45, hu_level = 10,
          logical_level = 1, linguistic_level = 1, kinesthetic_level = 1, musical_level = 1, visual_level = 1,
          naturalist_level = 1, group_level = 1, independent_level = 1)
        standards.objects.create(subject="Mathematics", standard="Counting", skill_topic = "Number range 0 - 100",
               objective = "Learners will count with and without using concrete objects and understand the need and convenience ofcounting in everyday life",
               competency = "count concrete objects up to 20and backwards from 20 - 0")
        activities.objects.create(school_lesson_id = 0,
           activity_title = "counting",
           subject="Mathematics",
           week_of = "September 18",
           standard = "Counting",
           intro = "bla",
           activity = "Count man.",
           wrap_up = "Did you count?",
           resources = "It's not that hard.",
           blooms = get_MI_BL("Count man."),
           vocabulary = "bla",
           day = "Wednesday")
        lesson_school_info.objects.create(school_lesson_id = 3,
           classroom = "unique", grade = "1st", school="anderson",
           week_of = "September 18",
           # date = 
           subject = "Mathematics",
           days = "Wednesday",
           objective = "Learners will count with and without using concrete objects and understand the need and convenience ofcounting in everyday life",
           planning_teacher = "cluc")
    def test_match_standard_activity(self):
        obj = lesson_school_info.objects.get(school_lesson_id=3)
        classroom = obj.classroom
        teacher_objective = obj.objective
        teacher_subject = obj.subject
        subject_summary = classroom_subject_summary.objects.filter(classroom=classroom)
        results_standards = match_standard(obj.objective, obj.subject )
        results_activities = match_activities("unique", obj.objective, results_standards[0], obj.subject)



